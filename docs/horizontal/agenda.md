Segue o conteúdo completo para o arquivo `docs/horizontal/agenda.md`, já estruturado de acordo com seu projeto ZapPRO:

---

### 📅 `agenda.md`

# Agenda Universal — Organização de Tarefas e Compromissos via WhatsApp

## Objetivo

A funcionalidade **Agenda** do ZapPRO oferece aos usuários a capacidade de organizar compromissos, lembretes e atividades diretamente pelo WhatsApp, utilizando linguagem natural. Ela visa substituir agendas físicas, Google Calendar ou aplicativos complexos, permitindo uma rotina mais fluida e automatizada com integração inteligente.

---

## Funcionalidades-Chave

| Função                       | Descrição                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------- |
| `Cadastrar compromisso`      | O usuário envia uma frase como "Tenho dentista amanhã às 14h" e o sistema agenda. |
| `Editar lembrete`            | Permite ajustes de hora, data, descrição ou tipo de evento.                       |
| `Listar compromissos`        | Retorna os compromissos do dia, semana ou período customizado.                    |
| `Excluir evento`             | Cancela eventos individuais com simples mensagens como “cancela dentista”.        |
| `Lembrete via WhatsApp`      | Envio automático de lembretes antes do compromisso (configurável).                |
| `Resumo diário automatizado` | Envio da agenda do dia toda manhã às 8h (opcional).                               |

---

## Estrutura de Armazenamento

* Banco: PostgreSQL ou MongoDB via backend FastAPI
* Tabelas/collections:

  * `agendas`: identificador do usuário, descrição, data/hora, lembrete configurado
  * `notificacoes`: fila de lembretes pendentes

---

## Integração com Orquestrador

* Mensagens com gatilhos de intenção como "lembra", "marcar", "anotar", "compromisso", "reunião", "agenda" são roteadas automaticamente ao agente `agenda_assistente`.
* O agente responde em linguagem natural e gera ações no banco via FastAPI.

---

## Estratégia de Trial vs PRO

| Versão Trial              | Versão PRO                                        |
| ------------------------- | ------------------------------------------------- |
| 3 compromissos por semana | Ilimitado                                         |
| Sem lembretes automáticos | Com lembretes por WhatsApp                        |
| Sem resumo diário         | Com resumo automatizado, recorrente e inteligente |

---

## Exemplo de Conversas

**Usuário**: "Me lembra da consulta com a Dra. Fernanda terça às 10h."
**Agente Agenda**: "Agendado com sucesso! Vou te lembrar 30 minutos antes, ok?"

---

## Possibilidades Futuras

* Exportar agenda em PDF com resumo da semana
* Sincronização com Google Calendar (via API externa)
* Agendamento por voz
* Compartilhamento da agenda com membros da equipe
