import os
import re
from fastapi import FastAPI, Request
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import httpx  # uso assíncrono em FastAPI

# 🔐 Carrega variáveis do .env
load_dotenv()

# 🚀 Inicializa app FastAPI
app = FastAPI()

# 🎯 Inicializa cliente GPT
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🌐 Dados da Z-API
ZAPI_ID = os.getenv("ZAPI_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_BASE_URL = os.getenv("ZAPI_BASE_URL")


@app.get("/")
def root():
    return {"status": "online", "mensagem": "Assistente Universal rodando com sucesso!"}


async def enviar_resposta(numero: str, mensagem: str):
    """Envia mensagem via Z-API para o número do WhatsApp"""
    url = f"{ZAPI_BASE_URL}/{ZAPI_ID}/send-message?token={ZAPI_TOKEN}"
    payload = {
        "phone": numero,
        "message": mensagem
    }
    try:
        async with httpx.AsyncClient() as client:
            await client.post(url, json=payload)
    except Exception as e:
        print(f"[ERRO] Falha ao enviar resposta via Z-API: {e}")


@app.post("/webhook/diario")
async def gerar_diario(request: Request):
    """
    Recebe dados via webhook da Z-API,
    gera um diário técnico em HTML com GPT-4
    e responde com link pelo WhatsApp
    """
    try:
        dados = await request.json()
        mensagem = dados.get("message", "")
        numero = dados.get("phone", "")

        # ✅ Verifica se mensagem começa com "diario:" (case insensitive)
        match = re.match(r"(?i)^di[áa]rio\s*:\s*(.+)", mensagem)
        if not match:
            return {"status": "ignorado", "motivo": "mensagem fora do padrão"}

        conteudo = match.group(1).strip()
        timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%M")
        nome_arquivo = f"diario_{numero}_{timestamp}.html"
        caminho = f"docs/diarios/{nome_arquivo}"
        link_final = f"https://zappro.site/diarios/{nome_arquivo}"

        # 🧠 Prompt inteligente para o GPT-4
        prompt = f"""Gere um diário técnico detalhado em HTML com seções:
✅ O que foi feito
🔍 Observações
🚧 O que faltou
🔁 Próximos passos
🧭 Sentimento do dia
📌 Destaque
⚠️ Atenção
Conteúdo do dia:
{conteudo}"""

        resposta = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        html = resposta.choices[0].message.content

        # 💾 Salva HTML no caminho final
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(html)

        # 📤 Envia link por WhatsApp
        await enviar_resposta(numero, f"✅ Diário gerado com sucesso!\n📄 {link_final}")

        return {"status": "ok", "arquivo": nome_arquivo, "link": link_final}

    except Exception as e:
        return {"status": "erro", "detalhes": str(e)}
