# 📚 Modelos de Resposta & Prompts – ZapPRO

**Resumo:**  
Aqui estão centralizados todos os modelos de resposta, prompts de agentes, exemplos de onboarding, fluxos de funil, textos prontos e templates que definem a experiência real do ZapPRO no WhatsApp.

---

## **Estrutura da pasta**

- `modelos_resposta.md`  
  Guia técnico: padrões de resposta, variáveis dinâmicas, exemplos para onboarding, vendas, fim de trial, etc.  
  *Use como referência ao criar ou revisar respostas automatizadas de qualquer agente.*

- `onboard_profissional.txt`  
  Exemplo real de onboarding invisível: copy para recepcionar usuário, captar perfil e engajar sem parecer cadastro.

- `prompt_agente_demo.txt`  
  Prompt mestre do agente demo: define estilo, missão, ferramentas, método Jab/Jab/Jab/Right Hook, limitações e regras de ouro.

- `prompt_agente_vendas.txt`  
  Prompt definitivo do agente de vendas: copywriting, técnicas de objeção, resposta curta e objetiva, sempre com CTA suave, anti-spam, humanizado.

---

## **Como usar esta pasta**

- Sempre revise e versiona qualquer alteração em prompts e modelos.
- Ao criar novo agente, sempre inicie a partir de um desses arquivos.
- Use o `modelos_resposta.md` como guia de compliance, boas práticas e limites (evita banimento, responde profissionalmente).
- Nunca exponha variáveis sensíveis (tokens, links privados) nos modelos.
- Atualize os exemplos sempre que o funil, oferta ou jornada de onboarding mudar.
- Se criar novo segmento/profissão, documente o prompt ou copy inicial.

---

## **Boas práticas**

- Todos os modelos devem parecer resposta de especialista humano, não robô.
- Limite de tokens por interação sempre claro (para evitar uso excessivo e travamentos).
- Finalize sempre com CTA que pareça “dica de parceiro”, nunca pressão de venda.
- Caso algum modelo fique ultrapassado, mova para `docs/modelos/old/` e registre no histórico.

---

## **Referências cruzadas**

- Os modelos desta pasta são usados diretamente pelos agentes definidos em `/agentes/`.
- Prompts também são base para treinamento de novos modelos IA/LLM.
- Compliance, direitos e limitações: ver `docs/horizontal/copywriter.md`.

---

> Atualizado em 2025-07-14  
> [Todos os direitos reservados | ZapPRO ©]
