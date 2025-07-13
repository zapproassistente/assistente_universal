# Decisões de Arquitetura – Projeto ZapPRO

Este documento registra as decisões técnicas, estratégicas e estruturais adotadas durante o desenvolvimento da plataforma **ZapPRO – Assistente Universal via WhatsApp**, visando organização, rastreabilidade e consistência do projeto.

---

## 📌 Objetivo da Documentação

- Justificar escolhas técnicas adotadas.
- Facilitar manutenção futura por qualquer desenvolvedor.
- Oferecer uma linha do tempo lógica e técnica para evolução do sistema.
- Auxiliar na transição para versões oficiais (ex: WhatsApp Business API).

---

## 🧱 Fundamentos da Arquitetura

| Decisão                                  | Justificativa                                                                 |
|------------------------------------------|-------------------------------------------------------------------------------|
| Utilizar containers isolados por agente  | Modularidade, escalabilidade e segurança isolada                              |
| Usar FastAPI como backend central        | Performance, simplicidade e fácil integração com serviços externos            |
| Utilizar Z-API (não oficial) inicialmente| Rápido para MVP e baixo custo, com controle interno de riscos                 |
| Criar agente fiscal separado             | Evitar banimentos por uso indevido do WhatsApp com moderação e auditoria     |
| Orquestrador de mensagens                | Centraliza controle, roteia e mantém o contexto do usuário                    |
| Controle de tokens por tempo/número      | Garantir limite justo para testes e planos pagos                              |
| Infra local no início, escalável na nuvem| Custo inicial reduzido e fácil migração posterior com Docker e Git            |

---

## 🔁 Evolução da Arquitetura

| Versão | Marco Evolutivo                                             |
|--------|-------------------------------------------------------------|
| 0.1    | Landing page funcional com direcionamento para WhatsApp    |
| 0.2    | Primeiro agente demo em funcionamento via Z-API            |
| 0.3    | Orquestrador + Agente Fiscal + FastAPI validador           |
| 0.4    | Containers para agentes especializados por profissão       |
| 0.5    | Integração com painel local e automações via script        |
| 0.6    | Sistema de upgrade via webhook e validação PRO             |
| 0.7    | Agente vendedor com IA embutida para upsell automático     |
| 1.0    | Transição planejada para WhatsApp Business API oficial     |

---

## 🔐 Segurança e Conformidade

- Toda mensagem passa obrigatoriamente pelo **Agente Fiscal**.
- Containers com isolamento de processo e de portas.
- Senhas e tokens centralizados em `.env` não versionado.
- Firewall habilitado no VPS (ufw).
- NGINX com headers de segurança ativados (X-Frame, X-Content-Type).
- Controle por IP/local para endpoints sensíveis (painel, monitoramento).

---

## 📤 Estratégia de Escalabilidade

- Estrutura baseada em `docker-compose` com rede isolada.
- Possível migração para Kubernetes (K8s) no futuro.
- Banco de dados em container, com possibilidade de externalizar.
- Volume persistente para dados sensíveis.
- CDN para a landing page (futuramente).

---

## ✅ Checkpoints Técnicos

| Item                                    | Status  |
|-----------------------------------------|---------|
| Container do FastAPI funcional          | ✅       |
| Z-API configurada e recebendo webhook   | ✅       |
| Agente Fiscal interceptando mensagens   | ✅       |
| Orquestrador roteando com lógica demo/PRO| ✅      |
| Tokens validados via número e tempo     | ✅       |
| Scripts locais para Git + Deploy        | ✅       |
| Landing page hospedada e funcional      | ✅       |
| Banco PostgreSQL conectado e persistente| ✅       |
| IA por agente com lógica modular        | 🔄 (em progresso) |
| Plano de migração para API oficial Meta | 🔄       |

---

## 🛠️ Ferramentas Utilizadas

| Ferramenta        | Função                              |
|-------------------|-------------------------------------|
| Docker            | Isolamento de containers            |
| FastAPI           | API Backend                         |
| PostgreSQL        | Banco de dados                      |
| Z-API             | Comunicação com WhatsApp (não oficial) |
| Git + GitHub      | Controle de versão                  |
| NGINX             | Servidor Web e Proxy Reverso        |
| Bash              | Automação de tarefas e deploy       |
| VS Code + SSH     | Edição remota no VPS                |

---

## 📚 Considerações Finais

A arquitetura do ZapPRO foi pensada desde o início para:

- **Escalar facilmente**: containers podem ser replicados ou migrados.
- **Segurança**: cada camada tem validação, controle e isolamento.
- **Controle**: o uso do WhatsApp não oficial é controlado rigorosamente.
- **Automação**: o projeto pode ser totalmente operado por script ou painel.
- **Conversão**: tudo foi desenhado para transformar um lead em usuário PRO de forma assistida por IA.

---

