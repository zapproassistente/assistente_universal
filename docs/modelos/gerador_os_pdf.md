# Gerador de Orçamento / Proposta / OS em PDF – Agente Demo e PRO

---

## Função no Demo (Jab, Jab, Jab)

- Usuário pode gerar até **2 PDFs gratuitos** (modelos minimalistas e modernos)
- Pode anexar a logo e/ou foto de assinatura
- Pode escolher entre:
    - Orçamento
    - Proposta Comercial
    - Ordem de Serviço (OS)
- **Onboarding embutido:** coleta nome da empresa, CNPJ, serviço, valor, condições, vencimento
- **Copy do agente:**
    - “Quer gerar um orçamento profissional em PDF para seu cliente?”
    - “Me envie sua logo e, se quiser, a assinatura. Posso montar agora mesmo!”
    - “Qual modelo você prefere? Minimalista ou clássico?”
    - “Orçamento pronto! No PRO, você libera modelos ilimitados, mais opções e histórico completo!”

## Função no PRO (Right Hook)

- PDFs ilimitados, modelos avançados (por profissão)
- Salva histórico (busca, duplicar, editar, re-enviar)
- Editor de modelos
- QR Code para PIX
- Integração com CRM (puxa cliente/serviço automático)
- Assinatura digital (imagem, foto, ou digitar nome)
- Download, envio por e-mail e WhatsApp
- Funil de conversão (“quantos orçamentos fechados/mês?”)

---

## Exemplo de Copy de Resposta:

**Demo:**
> “Pronto! Segue seu orçamento em PDF, personalizado. No PRO, você desbloqueia modelos, histórico e envio ilimitado. Quer liberar?”

**PRO:**
> “Orçamento criado, salvo no seu histórico. Você pode editar, duplicar, baixar, ou mandar por WhatsApp/e-mail. Mais alguma coisa?”

---

## Modelos

- **Minimalista**: Título, logo, serviço, valor, vencimento, observações, assinatura
- **Clássico**: Com detalhes, mais campos, rodapé com termos
- **Personalizado (PRO)**: Layouts por profissão, campos extra, branding completo

---

## Exemplo de chamada de endpoint (FastAPI):

`POST /gerar_pdf`
```json
{
  "tipo": "proposta",
  "cliente": "Maria Silva",
  "servico": "Consultoria de Marketing",
  "valor": "R$ 3.200",
  "logo_url": "https://zappro.site/logo.png",
  "assinatura_url": "https://zappro.site/assinatura.jpg",
  "modelo": "minimalista"
}
