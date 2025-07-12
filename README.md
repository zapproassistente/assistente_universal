# ASSISTENTE UNIVERSAL · Z-API + FASTAPI + GPT-4

## 🚀 VISÃO GERAL

Um sistema de atendimento inteligente que recebe mensagens via WhatsApp (Z-API), gera um diário técnico com GPT-4 e responde automaticamente ao remetente.

## ⚙️ FUNCIONALIDADES ATUAIS

* Conecta com Z-API para receber mensagens
* Usa FastAPI como servidor
* Integração com OpenAI GPT-4
* Gera diários técnicos em HTML
* Responde automaticamente pelo WhatsApp
* Containerizado com Docker e Docker Compose

---

## 📂 ESTRUTURA DO PROJETO

```
assistente_universal/
├── .env                    # Variáveis de ambiente (não subir)
├── .env.example           # Exemplo de arquivo .env
├── Dockerfile             # Imagem do container Python + FastAPI
├── docker-compose.yml     # Orquestração do container
├── requirements.txt       # Dependências Python
├── main.py                # App principal (FastAPI)
│
├── scripts/
│   └── diario_automation_local.py  # Gera diário localmente
│
├── docs/
│   ├── memoria/           # Logs ou memórias (futuro)
│   ├── diarios/           # Onde são salvos os HTMLs
│   │   └── vertical/
│   └── modelos/           # Templates, prompts, instruções
│
└── n8n/
    ├── n8n_diario_whatsapp.json  # Fluxo N8N
    └── README_n8n_diario.md      # Guia do N8N
```

---

## 📚 COMO USAR

### 1. PREPARAR O ARQUIVO `.env`

Copie o `.env.example` e insira:

```
OPENAI_API_KEY=...
ZAPI_ID=...
ZAPI_TOKEN=...
ZAPI_BASE_URL=...
```

### 2. SUBIR O PROJETO COM DOCKER

```bash
docker-compose up --build
```

### 3. ACESSAR FASTAPI

* Local: [http://localhost:8000](http://localhost:8000)
* Produção: [https://zappro.site](https://zappro.site)

### 4. ENVIAR MENSAGEM (EXEMPLO)

```
POST /webhook/diario
Body: Diario: Fiz ajustes no servidor e testei deploy
```

### 5. RESULTADO

* HTML gerado em `docs/diarios/`
* Confirmação enviada via Z-API WhatsApp

---

## 🚀 RUMO À VERSÃO FINAL

### 🌐 VISÃO DA ESTRUTURA FINAL IDEAL

```
assistente_universal/
├── backend/                  # FastAPI + lógica
│   ├── main.py
│   ├── services/
│   ├── models/
│   ├── api/
│   └── config/
├── frontend/                 # HTML, assets, landing page
│   ├── index.html
│   └── static/
├── infra/
│   ├── nginx/
│   ├── certbot/
│   └── docker/
├── .github/
│   └── workflows/         # CI/CD
├── tests/                    # Pytest ou similar
├── .env, .env.example
├── docker-compose.yml
└── README.md
```

### 🧵 PADRÕES E VERSÕES

* SemVer para versão do projeto (Ex: 0.1.0)
* `main` = branch estável
* `dev` = branch de desenvolvimento
* Uso de `.editorconfig` e `pre-commit`

### 📊 ETAPAS PARA CHEGAR LÁ

#### 🔄 CURTO PRAZO (v0.2.x)

* [ ] Gerar certificado SSL válido com Certbot
* [ ] Validar webhook Z-API com respostas reais
* [ ] Tornar variáveis dinâmicas (modelos, saídas)
* [ ] Melhorar layout do HTML gerado

#### ⚛️ INTERMEDIÁRIO (v0.5.x)

* [ ] Adicionar autenticação (token ou OAuth)
* [ ] Logs centralizados e dashboard
* [ ] CI/CD com GitHub Actions
* [ ] Monitoramento com Uptime Robot ou Prometheus

#### 🌟 VISÃO FINAL (v1.0.0)

* [ ] Infra como código (Terraform/Ansible)
* [ ] Modo multiusuário
* [ ] Dashboard frontend com histórico
* [ ] API para integrações externas
* [ ] Plano gratuito/pago com Stripe
* [ ] Deploy global com CDN e failover

---

## 💖 OBJETIVO MAIOR

> **Construir um produto de IA com nível de excelência OpenAI**: confiável, modular, documentado e pronto para escalar.

Claro! Abaixo seguem **dois prompts organizados e seguros**:

---

## ✅ PROMPT 1: ESTRUTURA DO PROJETO · CAMINHOS · IPS · DOMÍNIOS · SENHAS

> 🔐 **(Apenas para uso pessoal — mantenha esse prompt privado)**

```
Você está ajudando no projeto **Assistente Universal**, um sistema baseado em FastAPI + Docker + GPT-4 + Z-API com landing page e integração via WhatsApp.

📁 PASTAS IMPORTANTES (DENTRO DA VPS CONTABO):
- Código-fonte: `/home/stree/assistente_universal/`
- Arquivos HTML salvos: `/home/stree/assistente_universal/docs/diarios/`
- Arquivo de variáveis: `/home/stree/assistente_universal/.env`
- Arquivo Docker Compose: `/home/stree/assistente_universal/docker-compose.yml`
- Pasta pública do nginx (landing page): `/var/www/html/`

🌐 DOMÍNIOS:
- `zappro.site` ← apontando para VPS Contabo
- Subdomínios opcionais: `www.zappro.site`

🔑 ACESSOS CONHECIDOS:
- VPS IP: `187.112.70.54`
- Usuário da VPS: `stree` (usuário criado manualmente)
- Pasta home: `/home/stree`
- Último zip do projeto: `assistente_universal_2025-07-12.zip`

🔒 SENHAS DE VARIÁVEIS `.env`:
- `ZAPI_ID=3E301C0DF21DB35B5585`
- `ZAPI_TOKEN=s708E5371D77DA9BD3F8`
- `ZAPI_BASE_URL=https://api.z-api.io/instances`
- `OPENAI_API_KEY=oAsk525413ei9ZxbK7hC`
- `REFAC_PASS=Ju156458*`
```

---

## 📌 PROMPT 2: REGRAS DE PADRÃO · NOMEAÇÃO · BOAS PRÁTICAS

```
📋 Siga sempre estas REGRAS PADRÃO no projeto Assistente Universal:

✅ NOMES DE ARQUIVOS:
- Usar nomes claros e minúsculos com underline: exemplo → `main.py`, `gerador_diario.py`, `logo_zappro.png`
- Nunca sobrescreva arquivos finais sem gerar um backup com data: ex → `assistente_universal_2025-07-12.zip`

✅ NOMEAÇÃO DE VERSÕES:
- Usar padrão `ano-mes-dia` (YYYY-MM-DD) para zips e logs
- Cada pacote zipado deve seguir: `assistente_universal_YYYY-MM-DD.zip`

✅ ESTRUTURA FINAL DE PASTAS:
```

assistente\_universal/
├── main.py
├── docker-compose.yml
├── Dockerfile
├── .env
├── requirements.txt
│
├── docs/
│   └── diarios/
│       └── vertical/
│
├── scripts/
│   └── diario\_automation\_local.py
│
├── public\_html/
│   └── index.html (landing page)
│   └── logo.png

```

🚫 NÃO FAZER:
- Não deletar arquivos sem renomear ou backup
- Não alterar manualmente `.env` sem validar chaves
- Não executar comandos como root fora do WSL ou VPS sem entender

📌 FOCO:
- Projeto organizado como open-source
- Automatizado com CI/CD
- Escalável para múltiplos bots
- Seguro com padrão de arquivos imutáveis

```

---

Se quiser, posso transformar isso em dois arquivos:

* `infra_info.txt` (com acessos e caminhos)
* `regras_projeto.txt` (com as diretrizes)

Deseja que eu gere?


GIT COMIT CI

📌 REGRAS DIÁRIAS (para sincronizar sem sobrescrever nada)
🔼 Enviar do servidor → GitHub
bash
Copiar
Editar
cd /home/stree/assistente_universal
git add .
git commit -m "📦 Atualização na VPS - $(date +%F)"
git pull origin main --rebase
git push origin main
🔽 Atualizar do GitHub → servidor
bash
Copiar
Editar
cd /home/stree/assistente_universal
git pull origin main

