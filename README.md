### ✅ **Estrutura Refinada (Padrão por Container)**

Vamos adotar um padrão por **serviço isolado** (container), onde cada pasta representa **um agente ou função** com seu próprio ambiente, como se fosse uma “mini aplicação independente”.

#### **🌐 Raiz do Projeto (`assistente_universal/`)**

plaintext
assistente_universal/
├── agente-fiscal/              # Valida regras de compliance do WhatsApp
│   ├── Dockerfile
│   ├── main.py
│   ├── __init__.py
│   └── requirements.txt

├── fastapi/                    # API de comunicação central
│   ├── Dockerfile
│   ├── main.py
│   ├── __init__.py
│   └── requirements.txt

├── n8n/                        # Automação low-code (conector do ZapPRO)
│   └── [Dockerfile futuro se precisar]

├── orquestrador/              # Gerencia os agentes (router interno)
│   ├── Dockerfile
│   ├── main.py
│   ├── __init__.py
│   └── requirements.txt

├── scripts/                   # Utilitários para manutenção
│   ├── atualizar_painel.sh
│   ├── configurar_zappro.sh
│   ├── diario_automation_local.py
│   ├── git_pull.sh
│   ├── git_push.sh
│   ├── git_sync.sh
│   └── painel_assistente.sh

├── html/                      # Landing page
│   ├── index.html
│   ├── logo.png
│   └── Definido.png.Zone.Identifier (pode ser excluído)

├── docs/                      # Documentos e arquivos auxiliares
│   ├── memoria/
│   ├── diarios/
│   ├── modelos/
│   └── horizontal/vertical/

├── .env                       # Variáveis de ambiente principal
├── .env.example               # Exemplo do .env
├── .gitignore
├── docker-compose.yml        # Orquestra os serviços
├── Dockerfile                # (Opcional) Raiz, se for a imagem base
├── main.py                   # Entrada geral (se necessário)
└── README.md


---

### 🧩 **Padrão por Serviço (isolado por função)**

Cada `main.py` deve ter:

```python
# Exemplo básico
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}


E cada `Dockerfile`:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```

---

### 📦 **docker-compose.yml base**

```yaml
version: '3.8'
services:
  fastapi:
    build: ./fastapi
    ports:
      - "8000:8000"
    env_file:
      - .env

  orquestrador:
    build: ./orquestrador
    env_file:
      - .env

  agente-fiscal:
    build: ./agente-fiscal
    env_file:
      - .env


---


# ZapPRO - Assistente Universal via WhatsApp com FastAPI e Z-API

## Visão Geral

ZapPRO é uma plataforma SaaS escalável que oferece assistentes pessoais inteligentes via WhatsApp, integrando FastAPI para backend robusto e Z-API (não oficial) para comunicação com WhatsApp. O sistema possui um agente demo para trial, agentes especializados para usuários PRO, controle automático por número, funil de vendas via chat, onboarding disfarçado, e monitoramento de conformidade para evitar banimentos.

---

## Arquitetura

### Serviços e Containers

| Serviço             | Descrição                                                                                 | Tecnologia/Container                   |
|---------------------|-------------------------------------------------------------------------------------------|--------------------------------------|
| FastAPI Backend     | API RESTful para controle de usuários, trial, tokens, cadastro e lógica de negócios       | Container Docker com FastAPI          |
| Z-API               | Gateway WhatsApp para envio e recebimento de mensagens via API não oficial                | Container oficial [orkestral/docker-zap](https://github.com/orkestral/docker-zap) |
| Banco de Dados      | Armazena usuários, tokens, perfis, histórico de uso e status                              | Container PostgreSQL (ou MongoDB)    |
| Agente Fiscal       | Middleware que valida e modera mensagens para garantir conformidade com políticas da Meta| Container FastAPI separado           |
| Orquestrador        | Serviço que roteia mensagens entre agentes demo, especializados e fiscal                  | Container FastAPI                    |
| Agentes Especializados | Assistentes focados em tarefas específicas por profissão, ativados para usuários PRO   | Containers separados, FastAPI + IA   |
| Landing Page        | Página pública para conversão e direcionamento ao WhatsApp                                | Servida por NGINX ou CDN             |

---

## Fluxo de Usuário

1. Usuário acessa Landing Page e inicia conversa pelo WhatsApp via Z-API.
2. Z-API recebe mensagem e encaminha para Orquestrador via webhook.
3. Orquestrador verifica perfil do usuário no backend:
   - Se demo, direciona para Agente Demo.
   - Se PRO e demanda especializada, direciona para Agente específico.
4. Resposta gerada passa pelo Agente Fiscal para validação e moderação.
5. Resposta validada é enviada ao usuário via Z-API.
6. Sistema controla tokens e tempo de uso, gerando funil de upsell para PRO.
7. Usuário PRO tem acesso liberado a agentes avançados e funcionalidades adicionais.

---

## Componentes Técnicos

### FastAPI Backend

- Endpoints principais:
  - `/register`: Cadastro automático pelo número WhatsApp.
  - `/validate`: Verificação de tokens e status.
  - `/usage`: Controle de consumo e tokens.
  - `/upgrade`: Atualização para plano PRO.
- Gestão de usuários, tokens, histórico e planos.
- Integração com banco de dados relacional (PostgreSQL recomendado).

### Z-API

- Container oficial para comunicação WhatsApp não oficial.
- Configurado para webhook para receber e enviar mensagens.
- Comunicação síncrona com FastAPI backend para validação.

### Agente Fiscal

- Middleware intercepta e analisa mensagens.
- Aplica regras contra spam, conteúdo proibido e excesso de mensagens.
- Substitui respostas conforme política, registra logs e alertas.

### Orquestrador

- Serviço de roteamento de mensagens baseado em perfil e contexto.
- Despacha mensagens para agentes correspondentes.
- Centraliza controle e monitoramento.

### Agentes Especializados

- Containers isolados para cada tipo de agente.
- Implementados com FastAPI e integrações IA (ChatGPT, LangChain etc).
- Adaptados para profissões e usos específicos.

---

## Containerização (docker-compose.yml exemplo)

```yaml
version: '3.8'

services:
  fastapi:
    build: ./fastapi
    ports:
      - "8000:8000"
    volumes:
      - ./fastapi:/app
    env_file:
      - .env
    restart: always

  zapi:
    image: orkestral/docker-zap
    ports:
      - "8001:8001"
    volumes:
      - ./zapi_data:/usr/src/app/data
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: seu_usuario
      POSTGRES_PASSWORD: sua_senha
      POSTGRES_DB: zappro
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    restart: unless-stopped

  agente-fiscal:
    build: ./agente-fiscal
    ports:
      - "8002:8002"
    restart: always

  orquestrador:
    build: ./orquestrador
    ports:
      - "8003:8003"
    restart: always

  # Agentes especializados podem ser adicionados conforme necessário
````

---

## Segurança e Compliance

* Controle rigoroso via Agente Fiscal para evitar banimento.
* Armazenamento seguro e criptografado de dados sensíveis.
* Restrição de acesso por IP e autenticação JWT para APIs.
* Monitoramento constante e alertas de anomalias.

---

## Roadmap de Desenvolvimento

| Fase                       | Entregáveis principais                                     | Tempo estimado |
| -------------------------- | ---------------------------------------------------------- | -------------- |
| Integração FastAPI + Z-API | Endpoints básicos, webhook e comunicação                   | 2 semanas      |
| Agente Demo                | Funil trial, onboarding via WhatsApp, controle tokens      | 2 semanas      |
| Agente Fiscal              | Middleware para moderação e compliance                     | 3 semanas      |
| Orquestrador               | Roteamento dinâmico entre agentes                          | 3 semanas      |
| Agentes Especializados     | Containers com agentes para setores/profissões específicas | 4-6 semanas    |
| Sistema de Pagamento       | Links, notificações e ativação de planos PRO               | 3 semanas      |
| Migração Z-API oficial     | Testes e homologação para ambiente oficial                 | 4 semanas      |

---

## Como contribuir e colaborar

* Código versionado em GitHub com branches para cada feature.
* Pull requests revisados para qualidade e segurança.
* Documentação atualizada em `/docs`.
* Uso de testes automatizados e integração contínua.


```



# ✅ PROMPT DE MEMÓRIA GERAL — ASSISTENTE UNIVERSAL (ZAPPRO)

---

## 🔐 INFORMAÇÕES ESTRUTURAIS DO PROJETO

📁 **Pastas importantes na VPS (Contabo):**

```bash
/home/stree/assistente_universal/              # Código principal do projeto
/home/stree/assistente_universal/painel/       # HTML e arquivos do Painel Mestre
/home/stree/assistente_universal/scripts/      # Scripts de sincronização (git_sync.sh, painel_assistente.sh)
/var/www/painel/                               # Local final dos arquivos do painel
```

🌐 **Domínios e acesso:**

```text
https://zappro.site                 # Landing Page principal
https://painel.zappro.site          # Painel Mestre (Terminal Hacker Dev)
```

🔑 **Variáveis de ambiente do .env** (em `/home/stree/assistente_universal/.env`):

```env
ZAPI_ID=3E301C0DF21DB35B5585
ZAPI_TOKEN=s708E5371D77DA9BD3F8
ZAPI_BASE_URL=https://api.z-api.io/instances
OPENAI_API_KEY=oAsk525413ei9ZxbK7hC
REFAC_PASS=Ju156458*
```

🧠 **Usuário e conexão VPS:**

```text
Usuário VPS: stree
IP Contabo: 187.112.70.54
```

🔒 **SSH e GitHub:**

```bash
Chave pública SSH: /home/stree/.ssh/id_rsa.pub
Git remoto: git@github.com:ZapproAssistente/assistente_universal.git
```

---

## 📜 CHECKLIST PADRÃO (RADM) — COMO GERENCIAR O PAINEL

### 1️⃣ SUBIR ARQUIVOS HTML MANUALMENTE (PAINEL)

```bash
cp -r painel/* /var/www/painel/
sudo chown -R www-data:www-data /var/www/painel/
sudo systemctl reload nginx
```

### 2️⃣ USAR O SCRIPT `git_sync.sh` (para CI/CD simplificado)

```bash
sudo ./scripts/git_sync.sh
```
Esse script:
- Dá `git pull` do GitHub
- Dá push se tiver alterações
- Atualiza `/var/www/painel` automaticamente
- Reinicia o NGINX

### 3️⃣ TESTAR NGINX E DOMÍNIO

```bash
sudo nginx -t
sudo systemctl reload nginx
curl http://painel.zappro.site/teste.txt
```

### 4️⃣ OBTER CERTIFICADO SSL (LETSENCRYPT)

```bash
sudo certbot --nginx -d painel.zappro.site
```
(garanta que o domínio está apontando corretamente para a VPS)

---

## 📂 ESTRUTURA FINAL DO PROJETO (SONHADA)

```text
assistente_universal/
├── backend/           # FastAPI backend
├── frontend/          # HTML do painel e landing
├── scripts/           # Shell scripts úteis
├── docs/              # Diários gerados + modelos
├── infra/             # NGINX, certbot, docker
├── .env
├── docker-compose.yml
├── README.md
```

---

## 💡 PADRÕES DE NOMES E BACKUPS

✅ Sempre nomear arquivos com datas:

```bash
assistente_universal_2025-07-12.zip
```

✅ Nunca sobrescrever arquivos finais sem renomear antes.

---

## 🧪 TESTE DE SINCRONIZAÇÃO GIT CI

🔼 Enviar do servidor para GitHub:
```bash
cd ~/assistente_universal
git add .
git commit -m "📦 Atualização na VPS - $(date +%F)"
git pull origin main --rebase
git push origin main
```

🔽 Trazer do GitHub para o servidor:
```bash
cd ~/assistente_universal
git pull origin main
```

---
Perfeito. Aqui está um **prompt de visão estratégica**, bem estruturado, direto e pensado para orientar qualquer Dave (dev visionário) a entender **exatamente onde estamos** e **para onde estamos indo** com o projeto **Assistente Universal**:

---

## 🧠 **PROMPT DE MEMÓRIA E VISÃO ESTRATÉGICA DO PROJETO**

### 💡 CONTEXTO ATUAL · "ASSISTENTE UNIVERSAL" · **JULHO 2025**

Você está construindo um **painel IA modular**, com frontend minimalista estilo terminal ciano, totalmente inspirado em devtools como VS Code, WSL, Docker, NGINX e automações com N8N.
É um produto em **modo MVP funcional**, voltado a resolver o seguinte:

> 🔁 “Quero automatizar tudo que um dev faria manualmente: deploys, diários técnicos, comandos WSL, integração Z-API com WhatsApp, e feedback ao cliente.”

---

### ✅ **ONDE ESTAMOS AGORA**

📦 **Infraestrutura & Backend**

* FastAPI rodando via Docker (`docker-compose`)
* Integração com OpenAI GPT-4 para gerar diários técnicos
* Integração Z-API recebendo e enviando mensagens via WhatsApp
* VPS Contabo com NGINX servindo:

  * `zappro.site` → landing institucional
  * `painel.zappro.site` → painel de controle dev
* Painel pronto com botões de cópia de comandos (Git, Docker, WSL, etc.)

🗂 **Estrutura de pastas e CI**

```
assistente_universal/
├── painel/            # HTML e scripts do painel mestre
├── backend/           # FastAPI + lógica IA
├── docs/              # Diários HTML gerados
├── scripts/           # Shell scripts de automação
├── nginx/             # Blocos de config dos domínios
├── .env               # Chaves da OpenAI, Z-API, etc
```

🔐 **Autenticação via `.env` já funcional**
🚀 **Script `git_sync.sh` para deploy automático já implementado**

---

### 🔭 **VISÃO DE FUTURO (2025-2026)**

Se esse projeto fosse **meu como desenvolvedor**, aqui está o plano que seguiria até 1.0:

---

### 🔄 **0.5.x — Intermediário**

* 🔐 Autenticação do painel por token
* 🌈 Editor visual para HTML diário
* 📥 Webhook externo universal para receber tarefas (Z-API, Formulários, etc)
* 🔗 CI/CD: integração com GitHub Actions
* 📊 Dashboard com histórico de comandos executados

---

### 🌍 **1.0 — Escalável & Comercial**

* 🧑‍💻 Multiusuário (vários atendentes/consultores)
* 📂 Pastas protegidas por cliente (painel separado)
* 💬 Modo ChatGPT integrado ao frontend do painel
* 📦 Painel instalável via `pip` ou CLI (`pip install painel-zappro`)
* 🧠 Aprendizado de padrões: IA aprende como o dev trabalha e sugere ações
* 🌐 Página institucional pública com botão de "Entrar no Painel"
* 💳 Plano gratuito + Pro com integração Stripe

---

### 🔐 **2.0 — Plataforma Assistente AI Dev**

* 🧰 Repositório público com scripts para cada ferramenta (NGINX, AWS, Python, etc)
* 🤖 Modo "Sentry IA": monitora, responde, gera log e age
* 📈 Análise de produtividade técnica: quantos deploys, quantas respostas, histórico por projeto
* 🔁 Backup automático em S3/Cloudflare R2
* 💬 Logs em linguagem natural: "O que mudou neste deploy?"

---

### 🎯 OBJETIVO FINAL:

> Criar um **Painel Dev + IA + WhatsApp** onde qualquer dev (ou cliente) possa:
>
> 1. Automatizar processos técnicos
> 2. Registrar e gerar relatórios de tudo
> 3. Ser notificado, responder e acompanhar tudo via WhatsApp
> 4. Ter histórico acessível em HTML, via link
> 5. Expandir o produto como se fosse um “GitHub + ChatGPT + Deploy + Zap” em um só lugar.

---

### 📌 LINKS PARA ACESSO (ATUAL)

* **Painel:** [http://painel.zappro.site](http://painel.zappro.site)
* **Landing:** [https://zappro.site](https://zappro.site)
* **VPS IP:** `187.112.70.54`
* **Projeto:** `/home/stree/assistente_universal`
* **Deploy:** `/var/www/painel/index.html`

---

### 🛠 FALTAS TÉCNICAS CRÍTICAS AINDA PENDENTES:

* [ ] Adicionar chave SSH correta no GitHub
* [ ] Emitir e instalar SSL no `painel.zappro.site`
* [ ] Validar DNS do subdomínio
* [ ] CI/CD com autenticação automática e pull seguro

---

Se quiser, posso transformar este prompt em um PDF, Markdown ou arquivo de boas-vindas para qualquer dev ou cliente que entre no projeto. Quer que eu gere?

