# 📒 CRM Simples – ZapPRO

**Resumo:**  
Um CRM (Customer Relationship Management) **100% invisível**, sem fricção, que funciona direto no WhatsApp. O ZapPRO permite registrar, acompanhar, agendar follow-up e atualizar status de clientes via comandos simples, sem precisar de app ou painel externo.

---

## **Principais funções**

- ✅ **Cadastrar clientes novos:** “Cadastrar cliente Ana Pereira, setor vendas”
- ✅ **Registrar interesses ou pedidos:** “Ana quer proposta de consultoria”
- ✅ **Agendar follow-up automático:** “Me lembra de falar com Ana daqui 7 dias”
- ✅ **Marcar status do cliente:** “Ana – proposta enviada”
- ✅ **Listar clientes e status:** “Quem está aguardando resposta?”
- ✅ **Histórico de interações:** Disponível no PRO, com timeline

---

## **Exemplo de uso real**

**No WhatsApp:**
```

Usuário: Cadastrar cliente Carlos Silva, comprou consultoria
Bot: Cliente Carlos Silva cadastrado! Deseja agendar follow-up?
Usuário: Sim, para semana que vem.
Bot: Ok, agendado. Vou lembrar você pelo WhatsApp dia 22/07.

````

**Pela API (para dev):**
```json
POST http://localhost:8001/crm
{
  "mensagem": "Cadastrar cliente Joana, interesse em orçamento"
}
````

---

## **Como testar**

* **Via WhatsApp:**
  Envie comandos como “Cadastrar cliente Ana”, “Registrar interesse em X”, ou “Me lembra de falar com Y”.
* **Via API:**

  * Endpoint: `POST /crm`
  * Payload exemplo:

    ```json
    {
      "mensagem": "Cadastrar cliente Rafael, quer proposta financeira"
    }
    ```
  * Resposta esperada:

    ```json
    {
      "resposta": "Cliente Rafael cadastrado! Deseja agendar follow-up?"
    }
    ```

---

## **Diferença Trial vs PRO**

| Função                   | Trial/Demo       | PRO                            |
| ------------------------ | ---------------- | ------------------------------ |
| Cadastrar clientes       | ✅                | ✅                              |
| Agendar follow-up        | ✅ 1x por cliente | ✅ ilimitado                    |
| Histórico/timeline       | ❌                | ✅ (com exportação PDF/Excel)   |
| Segmentação por perfil   | ❌                | ✅ (vendas, suporte, parcerias) |
| Integração Google Sheets | ❌                | ✅ (fácil plugar/exportar)      |

---

## **Futuros upgrades**

* 🔄 Sincronização com Google Sheets/Drive
* 🗂️ Segmentação automática por funil (lead, proposta, cliente, perdido)
* 📊 Relatórios de conversão e performance
* 🤖 Ações automáticas baseadas em status (ex: enviar proposta automática)

---

> Atualizado em 2025-07-14
> \[Todos os direitos reservados | ZapPRO ©]

```
