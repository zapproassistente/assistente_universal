import sys
import logging
import json
from pathlib import Path

from orquestrador.utils.identificar_usuario import identificar_tipo_usuario
from orquestrador.utils.detectar_intencao import detectar_intencao
from orquestrador.utils.encaminhar_agente import encaminhar_para_agente
from orquestrador.utils.validar_compliance import validar_resposta_com_agente_fiscal
from orquestrador.utils.enviar_zapi import enviar_resposta_zapi

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class OrquestradorMine:
    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)

    def processar_mensagem(self, payload: dict):
        numero = payload.get("from")
        mensagem = payload.get("body")
        logging.info(f"📩 Mensagem recebida de {numero}: {mensagem}")

        tipo = identificar_tipo_usuario(numero)
        intencao = detectar_intencao(mensagem)
        resposta = encaminhar_para_agente(mensagem, tipo, intencao)
        resposta_segura = validar_resposta_com_agente_fiscal(resposta)

        enviar_resposta_zapi(numero, resposta_segura)

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
