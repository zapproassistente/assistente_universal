import sys
import logging
import json
import requests
from pathlib import Path

from orquestrador.utils.identificar_usuario import identificar_tipo_usuario
from orquestrador.utils.detectar_intencao import detectar_intencao
from orquestrador.utils.encaminhar_agente import encaminhar_para_agente
from orquestrador.utils.validar_compliance import validar_resposta_com_agente_fiscal
from orquestrador.utils.enviar_zapi import enviar_resposta_zapi

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

AGENTE_PROPOSTA_URL = "http://agente-proposta:8000/propostas/gerar"

class OrquestradorMine:
    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    def processar_mensagem(self, payload: dict):
        numero = payload.get("from")
        mensagem = payload.get("body")
        logging.info(f"📩 Mensagem recebida de {numero}: {mensagem}")

        tipo = identificar_tipo_usuario(numero)
        intencao = detectar_intencao(mensagem)

        # NOVO: Se a intenção for gerar proposta PRO, chama o novo agente
        if tipo == "pro" and intencao in ["proposta", "orcamento", "os"]:
            resposta = self.chamar_agente_proposta(payload)
        else:
            resposta = encaminhar_para_agente(mensagem, tipo, intencao)

        resposta_segura = validar_resposta_com_agente_fiscal(resposta)
        enviar_resposta_zapi(numero, resposta_segura)

    def chamar_agente_proposta(self, payload):
        # Extrai campos do payload conforme esperado pelo agente-proposta
        data = {
            "profissao": payload.get("profissao", "profissional"),
            "cliente": payload.get("cliente", "Cliente"),
            "servico": payload.get("servico", payload.get("body", "")),
            "valor": payload.get("valor", ""),
            "vencimento": payload.get("vencimento", ""),
            "termos": payload.get("termos", ""),
            "assinatura_texto": payload.get("assinatura_texto", ""),
            "status": payload.get("status", "pendente"),
            "modelo": payload.get("modelo", "personalizado"),
            "qrcode_pix": payload.get("qrcode_pix", ""),
            # NOTA: upload de arquivos (logo, assinatura, anexos) pode ser adicionado depois
        }
        try:
            response = requests.post(AGENTE_PROPOSTA_URL, data=data, timeout=15)
            if response.status_code == 200:
                json_data = response.json()
                # A resposta já traz copy pronta e link do PDF
                return json_data.get("copy_pronta", "Sua proposta PRO foi gerada!")
            else:
                return "❌ Erro ao gerar proposta PRO. Tente novamente ou entre em contato com o suporte."
        except Exception as e:
            logging.error(f"Erro ao chamar agente-proposta: {e}")
            return "❌ Erro de conexão ao gerar proposta PRO. Tente novamente em instantes."

    def run(self, arquivo_mensagem: str = None):
        logging.info("🚀 OrquestradorMine iniciado.")
        if arquivo_mensagem:
            with open(arquivo_mensagem, "r", encoding="utf-8") as f:
                payload = json.load(f)
            self.processar_mensagem(payload)
        else:
            logging.warning("⚠️ Nenhum arquivo de mensagem informado.")
        logging.info("✅ Execução finalizada.")

if __name__ == "__main__":
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    json_file = sys.argv[2] if len(sys.argv) > 2 else None
    orq = OrquestradorMine(base_dir=base_dir)
    orq.run(json_file)
