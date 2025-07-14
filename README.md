# 🚀 **ZAPPRO – Assistente Universal via WhatsApp**

**O SaaS modular definitivo: automação, inteligência, funil infinito e escala plugável, padrão multinacional.**

---

## 📦 **Estrutura Profissional e Modular**

```plaintext
assistente_universal/
├── agente-fiscal/       # 🛡️ Compliance WhatsApp/Meta, antifraude e anti-ban
├── agente-demo/         # 🎯 Funil de encantamento, onboarding, jab-jab-jab
├── agente-pro/          # 👑 Tudo do demo + ferramentas PRO e verticais
├── orquestrador/        # 🔄 Router entre agentes e API
├── fastapi/             # 🚀 API central de autenticação, tokens, usuários
├── html/                # 🌐 Landing page institucional
├── docs/                # 📚 Memória técnica, prompts, modelos, compliance
├── n8n/                 # ⚙️ Integrações e automações low-code
├── scripts/             # 🛠️ Deploy, backup, CI, manutenção
├── .env                 # 🔒 Variáveis sensíveis (NUNCA subir para git)
├── docker-compose.yml   # 🧩 Orquestra todos os serviços
└── README.md            # 📝 Este documento
```


# 🚀 Estrutura Completa do Projeto `assistente_universal/`

```plaintext
assistente_universal/
├── agentes/                         # Todos os agentes (microserviços FastAPI, Docker)
│   ├── agente-demo/                 # Agente Demo: onboarding, funil, trial (24h)
│   │   ├── __init__.py
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── agente-fiscal/               # Agente Fiscal: compliance WhatsApp/Meta, anti-spam
│   │   ├── __init__.py
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── agente-proposta/             # Gerador de Orçamento/Proposta/OS em PDF/MD
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── agente-pro/                  # Agente PRO: ferramentas premium/verticais/profissões
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   └── requirements.txt
│   └── orquestrador/                # Orquestrador: roteia mensagens entre agentes
│       ├── __init__.py
│       ├── Dockerfile
│       ├── main.py
│       └── requirements.txt
│
├── fastapi/                         # API central de autenticação e usuários
│   ├── __init__.py
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── docs/                            # Documentação, modelos, memória e decisões do projeto
│   ├── diarios/
│   │   ├── cliente_001.md           # Exemplo de interação
│   │   ├── interacao_trial.md
│   │   └── pontos_dor.txt
│   ├── horizontal/                  # (Docs de interface horizontal, se houver)
│   ├── memoria/                     # Memória técnica, arquitetura, lições, logs
│   │   ├── diarios_dev/
│   │   │   ├── checklist_deploy.md
│   │   │   ├── compliance_meta.md
│   │   │   ├── decisoes_arquitetura.md
│   │   │   ├── estrutura_tecnica.md
│   │   │   ├── glossario.md
│   │   │   ├── lições_aprendidas.md
│   │   │   ├── linha_do_tempo.md
│   │   │   ├── prompt_mestre.txt
│   │   │   ├── README.md
│   │   │   └── visao_geral.md
│   │   ├── log_tests/               # Pasta para logs automáticos de testes
│   │   │   └── README.md
│   ├── modelos/                     # Modelos prontos de resposta, prompt e onboarding
│   │   ├── modelos_resposta.md
│   │   ├── onboard_profissional.txt
│   │   ├── prompt_agente_demo.txt
│   │   └── prompt_agente_vendas.txt
│   ├── vertical/                    # Futuras verticais/profissões (ainda vazia)
│   └── README.md                    # Documentação do docs
│
├── html/                            # Landing page institucional e arquivos web
│   ├── index.html
│   ├── logo.png
│   ├── VSCode_git_aula.html         # Painel visual de comandos git/ci/cd
│   └── auto_gpt_agents_deploy.html  # Painel de deploy/expansão
│
├── n8n/                             # Integrações/automação low-code (plugue fácil)
│   └── (ainda vazio, reservado)
│
├── scripts/                         # Shell scripts utilitários de manutenção/ci/cd
│   ├── atualizar_painel.sh
│   ├── configurar_https.sh
│   ├── configurar_zappro.sh
│   ├── git_pull.sh
│   ├── git_push.sh
│   ├── git_sync.sh
│   ├── painel_assistente.sh
│   └── README.md
│
├── .env.example                     # Exemplo de variáveis de ambiente
├── .env                             # (NUNCA versionar! Variáveis reais)
├── .gitignore                       # Ignorar arquivos sensíveis
├── docker-compose.yml               # Orquestrador dos containers
├── requirements.txt                 # Requisitos globais do projeto (se usar)
└── README.md                        # Documentação principal do projeto
```

---

## **O que significa cada bloco?**

### **agentes/**

* Cada pasta = **um agente (microserviço) independente**, rodando seu próprio FastAPI, Dockerfile, requirements.txt.
* Plugável, escalável, cada um pode ser atualizado/expandido sem quebrar os outros.

### **fastapi/**

* Centraliza autenticação, tokens, cadastro de usuários, integração geral do sistema.
* Pode também ser um microserviço para orquestrar endpoints globais.

### **docs/**

* **diarios/**: exemplos de interações, conversas, casos reais.
* **memoria/diarios\_dev/**: arquitetura, decisões, aprendizados, checklist, compliance, lições do projeto.
* **modelos/**: prompts prontos, textos prontos, exemplos para IA.
* **vertical/**: espaço para profissões/segmentos que terão agentes específicos.
* **README.md**: resumo e guia dos arquivos do docs.

### **html/**

* Landing page, logo, painéis de comandos em HTML (foco em onboarding, vendas, e suporte dev).
* **index.html** é a entrada pública do produto.

### **n8n/**

* Integração low-code/sem código para automações externas: conectar WhatsApp ao Google Sheets, e-mail, API externas.

### **scripts/**

* **Shell scripts para manutenção, deploy, backup, CI/CD.**
* Sempre focado em facilitar a vida do dev/operador.

### **docker-compose.yml**

* Orquestra **todos os serviços/containers** do projeto (pode plugar, remover, escalar, rodar tudo junto).

### **.env.example / .env**

* Variáveis de ambiente (chaves, senhas, configs) — **.env NUNCA vai para o git!**

---

## **Regras de Ouro para Legado**

* **Documentação sempre atualizada** (qualquer mudança: docs/memoria, README).
* **Cada agente/microserviço é autônomo** (atualize sem quebrar outro).
* **Facilidade de onboarding:**
  Scripts, painéis, READMEs, tudo pronto para dev novo entender/rodar fácil.
* **Backup antes de grandes mudanças** (nomeie arquivos com data, sempre).
* **Expansão via container:**
  Quer criar novo agente? Copie um modelo de agente, mude o nome, ajuste Dockerfile, main.py, requirements.txt e registre no `docker-compose.yml`.



---

## 🧩 **Padrão Oficial por Serviço/Agente**

Cada agente (demo, fiscal, pro, orquestrador...) **é um microserviço FastAPI** 100% independente, sempre com:

* **main.py** padrão FastAPI (+ CORS, documentação)
* **requirements.txt** só com libs necessárias
* **Dockerfile** minimalista, expõe a porta do serviço

**Exemplo de `main.py`:**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Nome do Serviço/Agente",
    version="1.0.0",
    description="Descrição deste agente."
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
    return {"message": "API do Nome do Serviço está ativa"}
```

**Exemplo de `Dockerfile`:**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🧬 **Infraestrutura Completa (docker-compose.yml)**

**Plugue, escale, replique – só alterar, rodar e já está no ar!**

```yaml
version: '3.8'
services:
  fastapi:
    build: ./fastapi
    container_name: fastapi
    ports:
      - "8000:8000"
    volumes:
      - ./fastapi:/app
    env_file:
      - .env
    restart: always
    depends_on:
      - db

  orquestrador:
    build: ./orquestrador
    container_name: orquestrador
    ports:
      - "8001:8001"
    volumes:
      - ./orquestrador:/app
    env_file:
      - .env
    restart: always
    depends_on:
      - fastapi
      - db

  agente-fiscal:
    build: ./agente-fiscal
    container_name: agente-fiscal
    ports:
      - "8002:8002"
    volumes:
      - ./agente-fiscal:/app
    env_file:
      - .env
    restart: always
    depends_on:
      - db

  agente-demo:
    build: ./agente-demo
    container_name: agente-demo
    ports:
      - "8003:8003"
    volumes:
      - ./agente-demo:/app
    env_file:
      - .env
    restart: always
    depends_on:
      - db

  agente-pro:
    build: ./agente-pro
    container_name: agente-pro
    ports:
      - "8004:8004"
    volumes:
      - ./agente-pro:/app
    env_file:
      - .env
    restart: always
    depends_on:
      - db

  zapi:
    image: orkestral/docker-zap
    container_name: zapi
    ports:
      - "21465:21465"
    volumes:
      - ./zapi_data:/usr/src/app/data
    restart: unless-stopped

  db:
    image: postgres:15
    container_name: postgres
    environment:
      POSTGRES_USER: seu_usuario
      POSTGRES_PASSWORD: sua_senha
      POSTGRES_DB: zappro
    ports:
      - "5432:5432"
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:alpine
    container_name: redis
    ports:
      - "6379:6379"
    volumes:
      - ./redisdata:/data
    restart: unless-stopped

  n8n:
    image: n8nio/n8n
    container_name: n8n
    ports:
      - "5678:5678"
    volumes:
      - ./n8n_data:/home/node/.n8n
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=senha_forte
    restart: unless-stopped

volumes:
  pgdata:
  redisdata:
  n8n_data:
  zapi_data:
```

---

## ✨ **Visão & Diferenciais**

* **Assistente Universal/PRO via WhatsApp**

  * Demo (trial 24h) com onboarding disfarçado, ferramentas reais, funil infinito com copywriting jab-jab-jab-right hook
  * Agente PRO: +20 ferramentas, verticais por profissão, agenda, CRM, integrações, histórico, contabilidade
  * Conversa = venda sutil pro upgrade, nunca empurra-terapia
* **Compliance total:** Fiscal obrigatório, antifraude, monitoramento de tokens/uso, anti-ban
* **Arquitetura plugável/SaaS:** Cada agente é container, escala plugando, pronto para white label
* **Integrações low-code:** n8n para plugar WhatsApp → Google Sheets, CRM, email, visual

---

## 🛠️ **Como Rodar Local/Dev**

```bash
# 1. Clone o repositório
git clone git@github.com:ZapproAssistente/assistente_universal.git
cd assistente_universal

# 2. Ajuste o .env
cp .env.example .env
# (adicione chaves ZAPI, OpenAI, dados do Postgres, etc)

# 3. Suba os containers
docker-compose up --build -d

# 4. Acesse:
# FastAPI:        http://localhost:8000/docs
# Orquestrador:   http://localhost:8001/
# Agente Demo:    http://localhost:8003/
# Agente PRO:     http://localhost:8004/
# Landing Page:   /html/index.html (ou domínio via nginx)
```

---

## 🌐 **Deploy em Produção**

* **VPS (ex: Contabo) Ubuntu 22+, Docker, NGINX**
* **Domínio apontando para a VPS**
* **Scripts `/scripts/git_sync.sh`, `/scripts/painel_assistente.sh` para deploy**
* **Certbot para SSL grátis**
* **Backup diário (`assistente_universal_YYYY-MM-DD.zip`)**
* **Logs por container**

---

## 🔒 **Segurança, Pagamento e Blindagem**

* **Fiscal:** Bloqueia spam, abuso, uso indevido, responde conforme TOS WhatsApp/Meta
* **Pagamentos:** Recorrente via Stripe/Juno/Iugu/MercadoPago. Trial só cartão, antifraude, bloqueio automático
* **Webhook:** Ativa/desativa plano PRO após pagamento
* **Blacklist:** Por CPF, telefone, email, cartão
* **LGPD:** Cancelamento instantâneo
* **Env:** Fora do git sempre!

---

## 📈 **Roadmap/Futuro**

| Fase                | Entrega Principal                  | Status |
| ------------------- | ---------------------------------- | ------ |
| FastAPI + ZAPI      | Webhook, autenticação, trial       | ✅      |
| Agente Fiscal       | Compliance, monitoramento          | ✅      |
| Orquestrador        | Roteamento multi-agente            | ✅      |
| Agente Demo         | Funil, ferramentas de encantamento | ✅      |
| Agente PRO          | Verticais plugáveis                | 🚧     |
| Checkout Recorrente | Stripe/Juno, webhook               | ✅      |
| Landing pública     | HTML institucional                 | ✅      |

---

## 📂 **Padrão de Pastas e Comandos**

* **Scripts úteis:**

  * `/scripts/git_sync.sh` – CI/CD e deploy rápido
  * `/scripts/painel_assistente.sh` – Menu dev terminal
* **Backup:** Nomear com data (`assistente_universal_2025-07-14.zip`)
* **SSL:**

  ```bash
  sudo certbot --nginx -d zappro.site
  ```

---

## 📈 **Links Rápidos**

* **Landing Page:** [https://zappro.site](https://zappro.site)
* **GitHub:** `git@github.com:ZapproAssistente/assistente_universal.git`
* **VPS/IP:** `147.93.146.225` – Usuário: `stree`

---

## 🧩 **Como Expandir**

* Novo agente = nova pasta + Dockerfile + compose + registro de porta
* Plugue integrações n8n via compose
* Estrutura pronta para dashboard, multiusuário, franquia e white label

---

