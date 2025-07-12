# ASSISTENTE UNIVERSAL · Z-API + FASTAPI + GPT-4

## OBJETIVO
Receber mensagens via WhatsApp (Z-API), gerar um diário técnico com GPT-4 e responder automaticamente com confirmação.

## COMO USAR

### 1. CONFIGURAR ENV
Crie um arquivo `.env` na raiz com suas chaves (veja `.env.example`).

### 2. SUBIR O PROJETO
```bash
docker-compose up --build
```

### 3. ENDPOINT DISPONÍVEL
POST https://zappro.site/webhook/diario

### 4. FORMATO DA MENSAGEM
Envie via WhatsApp: `Diário: <seu texto>`

### 5. O QUE ACONTECE:
- Gera um HTML com base no texto
- Salva no servidor em `docs/diarios/`
- Envia confirmação via Z-API para o remetente


Claro! Aqui está o **conteúdo completo do `README.md`** em **formato claro, estruturado e em CAIXA ALTA** — com tudo o que você precisa saber **desde o começo até o funcionamento final** do projeto `assistente_universal`.

---

````markdown
# ASSISTENTE UNIVERSAL · DIÁRIO TÉCNICO AUTOMATIZADO

ESSE PROJETO PERMITE QUE VOCÊ ENVIE MENSAGENS (EX: PELO WHATSAPP OU CURL) COM O TEXTO DO SEU DIA DE TRABALHO, E O SISTEMA VAI:

✅ CONECTAR AO CHATGPT (GPT-4)  
✅ GERAR UM DIÁRIO TÉCNICO EM FORMATO HTML  
✅ SALVAR O ARQUIVO NO SEU WORKSPACE  
✅ (OPCIONAL) RODAR JUNTO COM O N8N PARA FLUXOS DE AUTOMAÇÃO VISUAL

---

## 🚀 COMO COMEÇAR

### 1. PRÉ-REQUISITOS

- TER DOCKER E DOCKER COMPOSE INSTALADO
- TER UMA CHAVE DA OPENAI (GPT-4)
- OPCIONAL: TER N8N INSTALADO (OU USAR O QUE VEM JUNTO NO DOCKER)

---

### 2. CONFIGURANDO O PROJETO

1. EXTRAIA O ARQUIVO `assistente_universal.zip`
2. ENTRE NA PASTA EXTRAÍDA:

```bash
cd assistente_universal
````

3. CRIE UM ARQUIVO `.env` COM SUA CHAVE:

```
OPENAI_API_KEY=sua_chave_aqui
```

---

### 3. SUBINDO O AMBIENTE

EXECUTE:

```bash
docker-compose up --build
```

VOCÊ VERÁ:

* FASTAPI RODANDO EM `http://localhost:8000`
* N8N DISPONÍVEL EM `http://localhost:5678`

---

### 4. ENVIANDO UM DIÁRIO

ENVIE UM POST PARA O WEBHOOK `/webhook/diario`

EXEMPLO COM `curl`:

```bash
curl -X POST http://localhost:8000/webhook/diario -d "DIÁRIO: HOJE MELHOREI O CÓDIGO DO FASTAPI E TESTEI O DEPLOY COM DOCKER."
```

✅ O HTML GERADO SERÁ SALVO EM:

```
docs/diarios/diario_DIA-MES-ANO.html
```

---

## 🧠 ESTRUTURA DO PROJETO

```
assistente_universal/
├── main.py                  ← API FASTAPI
├── docker-compose.yml       ← ORQUESTRAÇÃO DOS SERVIÇOS
├── Dockerfile               ← CONTAINER PYTHON + FASTAPI
├── requirements.txt         ← DEPENDÊNCIAS PYTHON
├── .env.example             ← MODELO PARA VARIÁVEIS DE AMBIENTE
│
├── scripts/
│   └── diario_automation_local.py ← GERA DIÁRIO LOCALMENTE
│
├── docs/
│   ├── memoria/
│   ├── diarios/
│   │   └── vertical/        ← ONDE FICAM OS HTMLS
│   └── modelos/             ← TEMPLATES E PROMPTS
│
└── n8n/
    ├── n8n_diario_whatsapp.json ← FLUXO IMPORTÁVEL NO N8N
    └── README_n8n_diario.md     ← INSTRUÇÕES DO FLUXO
```

---

## 🧩 COMO FUNCIONA

1. VOCÊ ENVIA UM TEXTO PARA O WEBHOOK
2. O FASTAPI PEGA O TEXTO E ENVIA PARA O GPT-4
3. O GPT GERA UM HTML PERSONALIZADO
4. O ARQUIVO É SALVO AUTOMATICAMENTE NO DISCO

---

## 🔄 INTEGRAÇÃO COM N8N (OPCIONAL)

1. ABRA `http://localhost:5678`
2. CLIQUE EM "IMPORT"
3. IMPORTE O ARQUIVO: `n8n/n8n_diario_whatsapp.json`
4. AJUSTE O CAMINHO DE SALVAMENTO
5. TESTE O FLUXO ENVIANDO UMA MENSAGEM PELO WHATSAPP OU HTTP

---

## 🛡️ DICAS DE SEGURANÇA

* **NUNCA SUBA SUA CHAVE `.env` PARA O GITHUB**
* USE `.gitignore` PARA IGNORAR O ARQUIVO `.env`
* MANTENHA SUA CHAVE SEGURA

---

## ✨ PRÓXIMOS PASSOS

* ADICIONAR MEMÓRIA COM REDIS OU SQL
* INTEGRAR COM GOOGLE SHEETS OU NOTION
* USAR TAGS PARA CATEGORIZAÇÃO INTELIGENTE
* MONTAR DASHBOARD COM SEUS DIÁRIOS

---

## 🧠 OBJETIVO DO PROJETO

TER UM ASSISTENTE PESSOAL INTELIGENTE QUE:

* CAPTA O QUE VOCÊ FEZ
* GERA UM DIÁRIO BONITO E FORMATADO
* SE LEMBRA DO CONTEXTO SEMPRE QUE PRECISAR
* PODE EVOLUIR COM VOCÊ, EM CÓDIGO, EM N8N OU NA NUVEM

---

```
