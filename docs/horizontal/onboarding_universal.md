Segue o conteúdo do arquivo `onboarding-universal.md`, pronto para ser colado:

---

# onboarding-universal.md

## Visão Geral

O objetivo deste documento é descrever a estratégia e as diretrizes para a construção de um processo de **onboarding universal automatizado** dentro da infraestrutura ZapPRO. Este processo ocorre integralmente via WhatsApp, utilizando agentes inteligentes que capturam dados, instruem o usuário e promovem conversões, sem fricção e sem necessidade de cadastro tradicional.

---

## Objetivos do Onboarding

* **Identificar o perfil do usuário** (profissão, objetivos, área de atuação).
* **Capturar dados relevantes** para segmentação e ativação de funcionalidades.
* **Educar o usuário** sobre os recursos disponíveis (versão trial e PRO).
* **Reduzir atrito** com cadastros e formulários tradicionais.
* **Atuar como pré-venda automatizada**, utilizando IA e persuasão conversacional.

---

## Estratégia Conversacional

O onboarding universal será orquestrado por um agente `demo`, que:

1. Recebe o novo usuário automaticamente assim que ele inicia a conversa via WhatsApp.
2. Inicia uma jornada guiada, onde faz perguntas simples com base em gatilhos psicológicos.
3. Apresenta respostas informativas, sempre encerrando com uma pergunta estratégica para seguir a jornada.
4. Utiliza recursos como:

   * Gatilhos mentais (curiosidade, exclusividade, urgência).
   * Linguagem informal e natural, adaptada ao público.
   * Captação progressiva (sem exigir tudo de uma vez).
5. Registra as respostas no banco de dados via FastAPI.

---

## Fases do Onboarding

| Fase             | Objetivo                                                                  |
| ---------------- | ------------------------------------------------------------------------- |
| 1. Saudação      | Acolher o usuário, explicar o que o assistente pode fazer por ele         |
| 2. Identificação | Perguntar o nome, área de atuação ou profissão                            |
| 3. Objetivo      | Descobrir o que o usuário busca: vender, organizar, automatizar etc.      |
| 4. Demonstração  | Apresentar uma funcionalidade principal com exemplo prático               |
| 5. Registro      | Armazenar dados relevantes no backend                                     |
| 6. Pitch PRO     | Apresentar o plano PRO e seus benefícios                                  |
| 7. Encerramento  | Reforçar suporte e que ele pode testar tudo gratuitamente por tempo/token |

---

## Integração Técnica

* O agente demo se conecta com o Orquestrador via Webhook.
* O Orquestrador redireciona o novo usuário para o fluxo de onboarding.
* O backend FastAPI recebe os dados em tempo real e atualiza a base de usuários.
* Tokens e tempo de uso são controlados por container de controle.

---

## Considerações Finais

* O onboarding universal é **obrigatório para todos os novos usuários**, mesmo que futuramente integremos com a API oficial da Meta.
* A linguagem deve ser revisada periodicamente com base em métricas de conversão.
* O modelo é extensível: pode ser adaptado por persona, nicho ou campanha de origem.

---
