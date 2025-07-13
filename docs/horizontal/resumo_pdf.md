Segue o conteúdo final do arquivo `resumo-pdf.md`, pronto para colar dentro do diretório `docs/horizontal/`:

---

# resumo-pdf.md

## Finalidade

O objetivo deste módulo é gerar automaticamente um **resumo em PDF personalizado** com os dados e interações do usuário com o assistente ZapPRO. Esse resumo pode ter múltiplas finalidades:

* Entregar valor ao usuário (resumo de insights, ações, tarefas).
* Atuar como ativo de conversão para o plano PRO.
* Registrar um relatório de uso ou performance de um agente.
* Fornecer um documento útil para clientes B2B (consultorias, clínicas, profissionais autônomos).

---

## Formato do Resumo

O PDF é gerado via FastAPI ou por um container especializado em geração de documentos. O conteúdo do resumo pode variar conforme o plano:

### Estrutura Comum (Trial e PRO)

* Nome do usuário (capturado no onboarding).
* Data e hora do resumo.
* Objetivo declarado do usuário.
* Lista das interações mais relevantes.
* Ações sugeridas pelo assistente.
* Observações automáticas com base nas mensagens.

### Elementos Exclusivos do PRO

* Gráficos ou estatísticas de performance (se aplicável).
* Recomendações de ferramentas IA baseadas no perfil.
* Campos personalizados por profissão.
* Assinatura do assistente especialista (por profissão).
* QR Code com link direto para continuidade no WhatsApp.

---

## Exemplo de Aplicação por Profissão

| Profissão        | Conteúdo Personalizado no PDF                                  |
| ---------------- | -------------------------------------------------------------- |
| Nutricionista    | Resumo alimentar, lista de metas, plano semanal proposto       |
| Mecânico         | Diagnóstico simulado e recomendações de manutenção             |
| Coach            | Frases motivacionais, metas da semana, progresso registrado    |
| Gestor Comercial | Pipeline simulado, script de vendas usado, índice de persuasão |
| Advogado         | Lista de demandas e prioridades, orientações básicas           |

---

## Tecnologias Envolvidas

* **FastAPI**: Endpoint `/generate-pdf` que recebe dados e retorna o PDF.
* **WeasyPrint** (ou similar): Biblioteca para converter HTML em PDF.
* **Jinja2**: Template engine para gerar HTML dinamicamente com base no usuário.
* **Banco de dados**: Consulta aos registros do usuário (tokens, profissão, uso).

---

## Gatilhos para Geração

* Comando do usuário (ex: "quero meu resumo").
* Final de sessão ou término do tempo trial.
* Proativamente pelo assistente como incentivo de upgrade.
* Periodicamente (se configurado para PRO mensal).

---

## Segurança e Armazenamento

* O PDF pode ser enviado diretamente via Z-API para o WhatsApp.
* Também pode ser armazenado temporariamente em `/pdf/usuário/{id}` com expiração automática.
* Nenhuma informação sensível deve ser salva sem criptografia ou consentimento explícito.

---

