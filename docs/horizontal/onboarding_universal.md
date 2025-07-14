# 🚀 Onboarding Universal – ZapPRO

**Resumo:**  
Onboarding automático, inteligente e sem fricção: o ZapPRO captura dados, entende perfil e necessidades do usuário, tudo via conversa natural no WhatsApp. Não exige formulário ou cadastro tradicional — o funil já vai convertendo enquanto encanta e entrega valor.

---

## **Principais funções**

- ✅ **Captação invisível:** Pergunta nome, profissão, necessidades, sem parecer cadastro
- ✅ **Segmentação automática:** Identifica se o usuário é MEI, autônomo, empresa, etc
- ✅ **Gatilhos de personalização:** Adapta as respostas e sugestões conforme respostas do lead
- ✅ **Micro-onboarding contínuo:** Coleta dados a cada nova interação, sem interromper a experiência
- ✅ **Pronto para upgrade:** Após 2-4 interações de valor, oferece o plano PRO de forma natural

---

## **Exemplo de fluxo real**

**No WhatsApp:**
```

Bot: Olá! Pode contar comigo. Quer ajuda para responder um cliente ou revisar um post?
Usuário: Quero revisar um post
Bot: Legal! Pra adaptar melhor, você trabalha com que tipo de negócio?
Usuário: Sou eletricista autônomo
Bot: Top! Se quiser, já posso salvar seu perfil. Assim, toda vez que pedir uma resposta já mando personalizada para eletricista.
Usuário: Sim, por favor
Bot: Perfil salvo! E se precisar de modelos prontos para orçamento ou cobrança, só avisar. ;)

````

---

## **Como testar**

- **Via WhatsApp:**  
  Inicie a conversa normalmente. Repare como o bot vai “puxando” informações sem pedir cadastro direto.
- **Via API:**  
  - Endpoint: `POST /onboarding`
  - Payload exemplo:  
    ```json
    {
      "mensagem": "Quero revisar uma mensagem"
    }
    ```
  - Resposta esperada:  
    ```json
    {
      "resposta": "Legal! Pra adaptar melhor, você trabalha com que tipo de negócio?"
    }
    ```

---

## **Diferença Trial vs PRO**

| Função                        | Trial/Demo      | PRO                              |
|-------------------------------|-----------------|----------------------------------|
| Coleta de perfil              | ✅ limitada     | ✅ detalhada (perfis múltiplos)  |
| Onboarding invisível          | ✅              | ✅ com histórico completo        |
| Upgrade automático            | ✅ convite leve | ✅ convite personalizado         |
| Integração CRM                | ❌              | ✅ plugável                      |

---

## **Futuros upgrades**

- 🤖 Onboarding por voz (transcrição automática)
- 🔄 Integração com CRM completo e segmentação de lista
- 🛒 Personalização de funil conforme área de atuação
- 🏷️ Etiquetas automáticas (lead quente, perdido, VIP...)

---

> Atualizado em 2025-07-14  
> [Todos os direitos reservados | ZapPRO ©]
````