import os
from datetime import datetime
from openai import OpenAI
import sys

openai = OpenAI()

def gerar_diario(content: str, workspace: str):
    data = datetime.now().strftime("%d/%m/%Y")
    prompt = f"Diário técnico de {data}:\n{content}"
    resp = openai.chat.completions.create(model="gpt-4", messages=[{"role":"user","content": prompt}])
    html = resp.choices[0].message.content
    nome = f"diario_{datetime.now().strftime('%d-%m-%Y')}.html"
    path = os.path.join(workspace, "docs", "diarios", nome)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Diário salvo em: {path}")

if __name__ == "__main__":
    content = sys.stdin.read().strip()
    workspace = os.path.abspath(os.path.dirname(__file__) + "/..")
    gerar_diario(content, workspace)