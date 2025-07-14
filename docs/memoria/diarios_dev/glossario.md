# 📖 Glossário de Termos – ZapPRO

**Resumo:**  
Lista de termos, siglas, nomes de agentes, containers e conceitos internos usados no projeto ZapPRO. Serve para facilitar onboarding de novos devs, esclarecer dúvidas em reuniões e evitar ruídos de comunicação.

---

## **Termos e definições**

- **ZapPRO**: Plataforma SaaS de assistentes pessoais/profissionais inteligentes via WhatsApp, com arquitetura modular e escalável.
- **Agente**: Serviço/container independente que executa funções específicas (ex: agenda, vendas, onboarding, financeiro).
- **Agente Demo**: Agente gratuito, com funções limitadas, focado em encantar, captar leads e introduzir o funil.
- **Agente PRO**: Agente pago, com funções completas, integrações extra e prioridade de suporte.
- **Agente Fiscal**: Middleware/serviço que valida, modera e monitora as mensagens, garantindo compliance com regras da Meta (WhatsApp).
- **Orquestrador**: Serviço que roteia as mensagens recebidas do WhatsApp, definindo para qual agente cada requisição deve ser enviada.
- **Funil Infinito**: Estratégia de vendas baseada em múltiplos “jabs” (entregas de valor) e CTAs suaves, mantendo o usuário sempre engajado.
- **Onboarding invisível**: Captação e cadastro de perfil do usuário feita de forma natural durante o uso, sem formulário explícito.
- **Trial**: Período de teste grátis com recursos limitados, objetivo de converter para o PRO.
- **Token**: Unidade de consumo, controle de limites de uso em cada agente.
- **Z-API**: API não oficial usada para integração com o WhatsApp.
- **Container**: Instância Docker que isola cada agente ou serviço, facilitando deploy, escala e manutenção.
- **Webhook**: Endpoint HTTP onde as mensagens do WhatsApp chegam e são processadas.
- **Compliance Meta**: Conjunto de práticas e limites para evitar bloqueios, banimento e problemas legais no WhatsApp/Meta.
- **Prompt Mestre**: Documento base com regras, visão, missão e identidade do produto — usado para treinamento e expansão.

---

## **Como usar**

- Sempre consulte este glossário antes de criar nomes para novos agentes ou funções.
- Adicione aqui novos termos, siglas ou conceitos sempre que surgir algo relevante.

---

> Atualizado em 2025-07-14  
> [Todos os direitos reservados | ZapPRO ©]
