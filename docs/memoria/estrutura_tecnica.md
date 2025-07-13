Perfeito. Vamos seguir com a estrutura e nomes exatos conforme seu projeto.

A seguir, o conteúdo inicial completo e pronto para colar no arquivo `docs/memoria/estrutura_artecnica.md`:

---

```markdown
# Estrutura Artécnica do Projeto ZapPRO

Este documento descreve a estrutura técnico-arquitetural do sistema **ZapPRO – Assistente Universal via WhatsApp**, detalhando os componentes, tecnologias, fluxos e organização do projeto, com foco em escalabilidade, modularidade e controle orquestrado por containers Docker.

---

## 📦 Estrutura de Pastas (Resumida)

```

assistente\_universal/
├── agente-fiscal/         # Validação e compliance das mensagens
├── fastapi/               # Backend de controle e lógica central
├── orquestrador/          # Router e distribuidor de mensagens
├── html/                  # Landing Page pública
├── scripts/               # Automação local e DevOps
├── docs/
│   └── memoria/           # Documentação técnica e decisões
├── .env                   # Variáveis de ambiente
├── docker-compose.yml     # Orquestração principal

````

---

## 🧠 Componentes Técnicos

### 1. **FastAPI Backend**
- Centraliza a lógica de negócio.
- Valida tokens, perfis e tempo de uso.
- Conecta com banco PostgreSQL.
- Expostos via endpoints `/register`, `/validate`, `/usage`, `/upgrade`.

### 2. **Orquestrador**
- Roteia mensagens entre os containers de agentes.
- Mantém o contexto e histórico da sessão.
- Redireciona para o agente correto: demo, fiscal ou PRO.

### 3. **Agente Fiscal**
- Avalia conteúdo antes do envio.
- Aplica regras contra spam, excesso de mensagens, links, vendas agressivas etc.
- Evita banimento por uso indevido da Z-API.

### 4. **Agentes Especializados (PRO)**
- Containers independentes com IA específica.
- Exemplo: agente de agenda, CRM, copywriter, social media, vendas, etc.
- Ativados após validação do plano.

### 5. **Z-API**
- Comunicação com WhatsApp não oficial.
- Requer cuidado extremo com limitação e moderação.
- Utiliza `webhooks` para envio e recebimento de mensagens.

---

## 🔁 Fluxo Geral

```mermaid
sequenceDiagram
    participant Usuário
    participant ZAPI
    participant Orquestrador
    participant FastAPI
    participant Agente Fiscal
    participant Agente Final

    Usuário->>ZAPI: Mensagem via WhatsApp
    ZAPI->>Orquestrador: Webhook com mensagem
    Orquestrador->>FastAPI: Verifica perfil
    FastAPI-->>Orquestrador: Status (Demo, PRO, Trial)
    Orquestrador->>Agente Fiscal: Passa mensagem
    Agente Fiscal->>Agente Final: Libera ou adapta
    Agente Final->>ZAPI: Resposta gerada
    ZAPI-->>Usuário: Entrega via WhatsApp
````

---

## 🧱 Tecnologias Utilizadas

| Componente     | Tecnologia                         |
| -------------- | ---------------------------------- |
| Backend        | Python + FastAPI                   |
| Agentes        | FastAPI + OpenAI API               |
| Mensageria     | Z-API (não oficial)                |
| Banco de Dados | PostgreSQL (local ou em container) |
| Orquestração   | Docker + docker-compose            |
| Servidor Web   | NGINX (Landing Page)               |
| Scripts DevOps | Bash Shell                         |

---

## 🔒 Segurança & Boas Práticas

* **Z-API com uso limitado e moderado.**
* **Monitoramento de IPs e uso de tokens.**
* Restrições via firewall e roteamento.
* Containerização isolada de agentes.
* Criptografia de `.env` sensíveis (fora do versionamento).
* Agente Fiscal como middleware obrigatório entre qualquer resposta.

---

## 🗺️ Próximos Passos (referente à estrutura técnica)

1. [ ] Criar script de provisionamento automático dos containers.
2. [ ] Implementar logs por container com roteamento central.
3. [ ] Configurar `.env` central com extensão modular por container.
4. [ ] Adicionar camada de cache (Redis) para controle de sessões.
5. [ ] Migrar o painel de controle para container próprio com login seguro.

---

## 🔁 Manutenção Contínua

Recomenda-se o uso do painel local (`painel_assistente.sh`) para:

* Deploy incremental.
* Testes por agente.
* Abertura automática no VS Code ou navegador.
* Git sync automatizado.







