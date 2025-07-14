from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import datetime

app = FastAPI(title="ZapPRO Agente Demo")

# --- MODELOS (simples, pode expandir depois)
class UserRequest(BaseModel):
    user_id: str
    message: str
    contexto: Optional[str] = None

# --- FUNÇÕES UTILITÁRIAS (cada função = ferramenta do Demo)
def gerar_resposta_venda(msg, perfil):
    # Simula análise de contexto e gera copy pronta (ajuste depois para LLM/prompt real)
    return f"Resposta de venda pronta para {perfil}: {msg} 🚀\nDica: Sempre destaque benefícios e use gatilhos de urgência!"

def mini_auditoria(whats, insta):
    return f"""Mini auditoria:\nWhatsApp: {whats}\nInstagram: {insta}\nSugestão: Ajuste sua bio com chamada para ação e use imagem profissional."""

def orcamento(cliente, servico, valor):
    return f"""📋 ORÇAMENTO\nCliente: {cliente}\nServiço: {servico}\nValor: R$ {valor}\nInclui material? Garantia de 6 meses."""

def agenda_do_dia(area):
    return f"""Agenda do dia para {area}:\n1. Fazer follow-up com clientes\n2. Revisar propostas\n3. Criar conteúdo para redes sociais"""

def ideia_post(area):
    agora = datetime.datetime.now().strftime("%Hh")
    return f"""Post para {area}: 'Hoje às {agora}, compartilhe um case de sucesso!'\nLegenda: 'Mostre seu resultado! #NegócioLocal'"""

def roteiro_video(area):
    return f"""Roteiro de vídeo ({area}):\n1. Apresente-se em 10s\n2. Mostre 1 solução que resolve dor do cliente\n3. Chame para o WhatsApp"""

def controle_gastos():
    return "Envie suas despesas e receitas. No fim do dia, te mando um resumo separando pessoal/PJ."

def benchmarking(area):
    return f"No seu segmento ({area}), os melhores postam todo dia, respondem clientes em até 5min e atualizam o status semanalmente."

def dicas_fiscais():
    return "Dica fiscal: mantenha sempre suas notas organizadas e evite enviar lista para muitos contatos ao mesmo tempo no WhatsApp!"

def resumo_do_dia(user_id):
    # Placeholder para histórico
    return f"Resumo do seu dia, {user_id}: 2 propostas enviadas, 1 venda fechada, 3 clientes para follow-up amanhã."

# --- ROTAS FASTAPI (cada função pode ser plugada no orquestrador)

@app.post("/resposta-venda")
def resposta_venda(req: UserRequest):
    perfil = req.contexto or "comercial"
    resposta = gerar_resposta_venda(req.message, perfil)
    return {"resposta": resposta}

@app.post("/auditoria")
def auditoria(req: UserRequest):
    whats = req.message
    insta = req.contexto or ""
    resposta = mini_auditoria(whats, insta)
    return {"resposta": resposta}

@app.post("/orcamento")
def criar_orcamento(req: UserRequest):
    dados = req.message.split(";")
    cliente = dados[0] if len(dados) > 0 else "Cliente"
    servico = dados[1] if len(dados) > 1 else "Serviço"
    valor = dados[2] if len(dados) > 2 else "Valor não informado"
    resposta = orcamento(cliente, servico, valor)
    return {"resposta": resposta}

@app.post("/agenda")
def agenda(req: UserRequest):
    area = req.contexto or "negócio"
    resposta = agenda_do_dia(area)
    return {"resposta": resposta}

@app.post("/post")
def post(req: UserRequest):
    area = req.contexto or "negócio"
    resposta = ideia_post(area)
    return {"resposta": resposta}

@app.post("/roteiro-video")
def roteiro(req: UserRequest):
    area = req.contexto or "negócio"
    resposta = roteiro_video(area)
    return {"resposta": resposta}

@app.post("/gastos")
def gastos(req: UserRequest):
    resposta = controle_gastos()
    return {"resposta": resposta}

@app.post("/benchmarking")
def bench(req: UserRequest):
    area = req.contexto or "negócio"
    resposta = benchmarking(area)
    return {"resposta": resposta}

@app.post("/dica-fiscal")
def fiscal(req: UserRequest):
    resposta = dicas_fiscais()
    return {"resposta": resposta}

@app.post("/resumo")
def resumo(req: UserRequest):
    resposta = resumo_do_dia(req.user_id)
    return {"resposta": resposta}

@app.get("/menu")
def menu():
    return {
        "menu": [
            "resposta-venda", "auditoria", "orcamento", "agenda", "post", "roteiro-video",
            "gastos", "benchmarking", "dica-fiscal", "resumo"
        ],
        "dica": "Chame qualquer função digitando seu nome!"
    }

# --- Funil Infinito e CTA embutido (pode ser chamado pelo orquestrador ao fim de X interações)
@app.get("/cta-pro")
def cta():
    return {
        "mensagem": "Gostou? Ative todas as funções PRO agora e teste por 7 dias sem risco — se não gostar, cancela e recebe 100% de volta. Aqui é zero enrolação."
    }
