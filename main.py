import os
import requests
from fastapi import FastAPI, Request
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ZAPI_ID = os.getenv("ZAPI_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_BASE_URL = os.getenv("ZAPI_BASE_URL")

def enviar_resposta(numero: str, mensagem: str):
    url = f"{ZAPI_BASE_URL}/{ZAPI_ID}/send-message?token={ZAPI_TOKEN}"
    payload = {
        "phone": numero,
        "message": mensagem
    }
    requests.post(url, json=payload)

@app.post("/webhook/diario")
async def receber_mensagem(request: Request):
    dados = await request.json()
    msg = dados.get("message", "")
    numero = dados.get("phone", "")

    if not msg.lower().startswith("diário:"):
        return {"status": "ignorado"}

    conteudo = msg.split(":", 1)[1].strip()
    data = datetime.now().strftime("%d-%m-%Y")

    prompt = f"""Aja como um diário técnico inteligente.
Receba o conteúdo a seguir e gere um HTML com:
✅ O que foi feito
🔍 Observações
🚧 O que faltou
🔁 Próximos passos
🧭 Sentimento do dia
📌 Destaque
⚠️ Atenção
Conteúdo:
{conteudo}"""

    resposta = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    html = resposta.choices[0].message.content
    caminho = f"docs/diarios/diario_{data}.html"
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(html)

    link = f"https://zappro.site/diarios/diario_{data}.html"
    enviar_resposta(numero, f"✅ Diário gerado com sucesso! Veja aqui: {link}")

    return {"status": "ok", "link": link}
