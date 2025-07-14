from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ZapPRO Agente PRO",
    version="1.0.0",
    description="Agente PRO do ZapPRO — Assistente pessoal/profissional avançado para WhatsApp, integrado com IA, automações e funções plugáveis por profissão."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ZapPRO Agente PRO ativo e rodando."}

@app.post("/resposta-venda")
async def resposta_venda(request: Request):
    body = await request.json()
    mensagem = body.get("message", "")
    profissao = body.get("profissao", "negócio")
    # Resposta PRO ultra personalizada (exemplo simples)
    return {
        "resposta": f"[PRO] Resposta premium para {profissao}: {mensagem}\nDica PRO: use gatilhos de autoridade e benefícios exclusivos na sua resposta."
    }

@app.post("/agenda-inteligente")
async def agenda_inteligente(request: Request):
    body = await request.json()
    profissao = body.get("profissao", "negócio")
    return {
        "agenda": [
            "8h - Revisão de propostas",
            "10h - Reunião com equipe",
            "14h - Produção de conteúdo avançado",
            "16h - Follow-up PRO com clientes VIP"
        ],
        "dica": f"Sua agenda PRO já integra Google/Outlook para {profissao}!"
    }

@app.post("/relatorio-rede-social")
async def relatorio_rede_social(request: Request):
    body = await request.json()
    perfil = body.get("perfil", "empresa")
    return {
        "relatorio": f"Seu Instagram {perfil} atingiu +30% engajamento. Sugestão: poste às 18h com stories interativos PRO.",
        "copy": "Exemplo de copy PRO: 'Hoje mostro bastidores do meu trabalho! [Seu diferencial]'"
    }

@app.post("/financeiro")
async def financeiro(request: Request):
    body = await request.json()
    gastos = body.get("gastos", [])
    total = sum(gastos) if gastos else 0
    return {
        "resumo": f"Gastos do dia: R$ {total}. Projeção PRO feita, gráfico pronto!",
        "dica": "No PRO, você recebe análise financeira semanal direto no WhatsApp!"
    }
