# Linha do Tempo – ZapPRO

Este documento registra os marcos técnicos e decisões estratégicas da construção da plataforma **ZapPRO – Assistente Universal via WhatsApp**, orientada para escalabilidade, modularidade e conformidade com as diretrizes da Meta.

---

## 🔹 2025-07-01 – Concepção do Projeto

- Definição da visão SaaS: assistente pessoal via WhatsApp com agentes especializados.
- Estrutura inicial baseada em **containers Docker** e API com **FastAPI**.
- Escolha da **Z-API (não oficial)** como ponte inicial com o WhatsApp.

---

## 🔹 2025-07-02 – Organização Modular

- Criação das pastas `agente-fiscal`, `fastapi`, `orquestrador` e `html`.
- Definição dos primeiros scripts de automação: `git_sync.sh`, `painel_assistente.sh`.
- Estruturação da landing page em `/html/index.html`.

---

## 🔹 2025-07-03 – Implantação da VPS

- Configuração da **VPS Contabo Ubuntu 22.04**.
- Instalação do Docker, Docker Compose, NGINX.
- Configuração dos domínios `zappro.site` e `painel.zappro.site`.

---

## 🔹 2025-07-04 – Integração de Componentes

- Conexão do FastAPI com Z-API.
- Primeiros testes com roteamento de mensagens via Orquestrador.
- Implantação do **Agente Demo** com lógica de onboarding disfarçado e funil de upsell.

---

## 🔹 2025-07-05 – Compliance e Segurança

- Criação do **Agente Fiscal** para intermediar mensagens e validar conteúdo.
- Implementação de restrições de IP no NGINX local.
- Validação de regras para evitar banimento no uso da Z-API.

---

## 🔹 2025-07-06 – Estrutura de Logs e Documentação

- Criação da pasta `docs/memoria/log_tests/` com `README.md`.
- Início da documentação técnica com `decisoes_arquitetura.md` e `estrutura_tecnica.md`.

---

## 🔹 2025-07-07 – Definição da Arquitetura de Agentes

- Planejamento de agentes por profissão (com base na CBO).
- Definição de containers independentes por tipo de agente.
- Criação do agente de **resposta adesiva comercial** para leads dos clientes PRO.

---

## 🔹 2025-07-08 – Roadmap de Evolução

- Planejamento da migração futura para API oficial do WhatsApp (Meta).
- Definição da hierarquia de agentes: Demo → Fiscal → Especializados.
- Registro do plano de uso de **LangChain**, **Redis**, e **N8n** como extensões futuras.

---

## 🔹 Próximos Passos

- Finalização e testes da integração completa com `docker-compose`.
- Ativação dos primeiros agentes por profissão.
- Implantação de modelo de cobrança (trial + plano PRO via Pix ou API externa).
- Criação de **logs de uso por número** e painel de controle do backend.

---

> ⚙️ Esta linha do tempo será atualizada à medida que o ZapPRO evolui.
