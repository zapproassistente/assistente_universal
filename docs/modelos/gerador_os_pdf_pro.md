# Gerador Universal de Proposta/Orçamento/OS – AGENTE PRO

---

## Funções exclusivas do PRO

- Geração de PDFs **ilimitados** e personalizáveis
- Escolha entre modelos por profissão/setor (advogado, eletricista, médico, coach, agência, oficina, etc)
- **Editor visual:** usuário monta campos, logotipo, cores, rodapé, fotos, assinatura, termos extras
- **Assinatura digital**: por upload de imagem, desenhar no painel ou digitar nome
- **QR Code PIX integrado** (paga na hora!)
- **Histórico de propostas:** busca, filtra, duplica, reenvia, exporta (Excel/PDF)
- **Status de cada proposta:** pendente, aceita, recusada, cancelada
- **Envio automático por WhatsApp, e-mail, download ou link compartilhável**
- **Integração CRM:** já puxa os dados do cliente/negociação para preencher a proposta automaticamente
- **Anexos extras:** fotos do serviço, documentos, contratos, recibo

---

## Fluxo de Uso (PRO)

1. Usuário escolhe ou cria modelo (padrão por profissão ou novo via editor visual)
2. Preenche campos dinâmicos (cliente, serviço, valor, vencimento, condições)
3. Faz upload de logo e assinatura (imagem/foto)
4. (Opcional) Adiciona QR Code para pagamento imediato (ex: PIX)
5. Gera PDF personalizado (branding removível)
6. Salva no histórico, com opção de editar, duplicar, reenviar, exportar Excel
7. Marca status (aceita, recusada, etc)
8. (Opcional) Envia por WhatsApp, e-mail, ou link

---

## Exemplos de Copy para o PRO

- “Proposta criada e salva no seu histórico! Quer duplicar ou editar para outro cliente?”
- “Inclua QR Code PIX e aumente suas chances de fechar negócio na hora.”
- “Assinatura digital pronta! Cliente pode assinar direto pelo celular.”
- “No painel PRO, todos seus PDFs ficam salvos, você exporta para Excel e monitora o status de cada negociação.”

---

## Exemplo de Endpoint FastAPI (para geração de PDF avançado)

`POST /propostas/gerar`

```json
{
  "tipo": "os",
  "profissao": "eletricista",
  "cliente": "João Souza",
  "servico": "Manutenção elétrica predial",
  "valor": "R$ 900",
  "logo_url": "https://zappro.site/uploads/eletricista_logo.png",
  "assinatura_url": "https://zappro.site/uploads/assinatura_joao.png",
  "modelo": "personalizado",
  "qrcode_pix": "0002012658...",
  "anexos": ["https://zappro.site/uploads/foto01.jpg"],
  "termos": "Garantia de 12 meses.",
  "status": "pendente"
}
