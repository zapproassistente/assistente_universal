# 📚 Memória Técnica — Projeto ZapPRO

Este documento serve como repositório de decisões, padrões arquiteturais, ideias evolutivas e aprendizados durante o desenvolvimento da plataforma **ZapPRO**, um sistema de assistentes inteligentes via WhatsApp (Z-API), com backend em FastAPI e escalável via containers.

---

## 🔧 Justificativa do Projeto

ZapPRO nasce da necessidade de criar um **funil de vendas inteligente**, operado via WhatsApp, que:
- Integra **assistentes especializados por profissão**.
- Automatiza **cadastro**, **onboarding** e **upsell para plano PRO**.
- Respeita as **limitações da API não-oficial** enquanto antecipa a migração futura para APIs oficiais da Meta.

---

## 📦 Estrutura Modular

A estrutura é composta por múltiplos containers independentes, organizados por responsabilidade:

| Componente         | Descrição                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `fastapi/`         | Backend que controla usuários, tokens, planos e integra com os agentes    |
| `zapi/`            | Conector com o WhatsApp (via container Orkestral/docker-zap)              |
| `orquestrador/`    | Roteador de mensagens entre agentes, fiscal e backend                     |
| `agente-fiscal/`   | Valida as mensagens para evitar spam, banimento ou violação de regras     |
| `agentes-pro/`     | Containers com IA por profissão para usuários PRO                         |
| `html/`            | Landing page com redirecionamento direto para WhatsApp (sem formulário)   |
| `docs/`            | Documentação do projeto                                                    |

---

## 🧠 Decisões Técnicas

- Uso de **Z-API não oficial**: rápido para validar o MVP, com planos para migração futura.
- Contêiner separado para **fiscalização e conformidade** com regras da Meta.
- Agente `demo` encapsula onboarding, vendas e controle de tempo/token.
- **Persistência em PostgreSQL**, com estrutura flexível para usuários e históricos.
- **Agentes por profissão** são carregados sob demanda, evitando consumo excessivo.
- Integração futura com **API oficial da Meta** já prevista na arquitetura.

---

## 🔐 Segurança

- Acesso IP restrito para painel administrativo (removido no modo local).
- Logs e validação por agente-fiscal para evitar spam.
- Tokens por tempo e número para limitar o uso gratuito e evitar abusos.
- Sem armazenamento de dados sensíveis no frontend (html), apenas redirecionamento.

---

## 📈 Planos de Evolução

- Implementar plano PRO com pagamento via Pix ou link externo.
- Adicionar autenticação por QR Code para gestão PRO.
- Implementar dashboard administrativo com monitoramento de sessões e uso.
- Desenvolver orquestrador inteligente com priorização de carga.
- Adicionar suporte a múltiplos idiomas automaticamente detectados.

---

## 🗂 Registro de Iterações

Todas as alterações estruturais são registradas no diretório [`docs/diarios`](../diarios/), com data, autor e contexto da modificação.

---

## ✍️ Autor

> Este projeto é arquitetado por Will, com apoio do ChatGPT como copiloto de IA, visando uma solução escalável, automatizada e amigável para empreendedores digitais brasileiros.

