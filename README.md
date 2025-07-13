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

