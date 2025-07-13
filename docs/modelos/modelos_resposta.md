Perfeito. Abaixo está uma versão **profissional, técnica e orientada a produto final** do arquivo `modelos_resposta.md`, com foco em consistência, clareza e aplicação real no ambiente corporativo:

---

```markdown
# modelos_resposta.md

## Diretrizes Técnicas para Modelos de Resposta – Sistema ZapPRO

Este documento estabelece o padrão formal e técnico para a construção das respostas automatizadas utilizadas pelos agentes do sistema ZapPRO. Os modelos devem prezar por precisão, adequação contextual e linguagem profissional, considerando tanto usuários em fase de avaliação (TRIAL) quanto usuários assinantes (PRO).

---

## 1. Finalidade dos Modelos

Os modelos de resposta são utilizados para:

- Respostas automatizadas em conversas iniciadas via WhatsApp;
- Personalização por categoria profissional (via ROMs);
- Fluxos de onboarding invisível (cadastro orientado por diálogo);
- Gatilhos de venda automatizados (funil comercial);
- Controle de comportamento dos agentes (linguagem, tom, escopo);
- Comunicação proativa com base em eventos do sistema (ex: fim de trial, aviso de limites).

---

## 2. Estrutura Formal das Respostas

As respostas geradas por qualquer agente devem seguir a estrutura padronizada abaixo, salvo exceções justificadas tecnicamente:

```

\[Contexto lógico identificado]
\[Resposta clara e objetiva ao input do usuário]
\[Complemento com valor técnico ou sugestão de próxima ação]
\[Call-to-action (CTA) se aplicável, com link ou botão inteligente]

```

Todos os blocos devem ser avaliados em tempo de execução, com base em parâmetros da sessão (tempo, plano, tipo de interação e perfil profissional).

---

## 3. Padrão de Variáveis Dinâmicas

Os placeholders utilizados nos modelos devem estar integrados ao sistema de substituição do orquestrador e seguir nomenclatura clara e consistente. Exemplos:

| Variável             | Descrição                                        |
|----------------------|--------------------------------------------------|
| `{{nome}}`           | Nome do usuário (extraído do WhatsApp)           |
| `{{profissao}}`      | CBO ou profissão declarada                       |
| `{{plano}}`          | Nível do plano: TRIAL ou PRO                     |
| `{{tokens_restantes}}`| Quantidade estimada de uso restante              |
| `{{link_upgrade}}`   | URL do painel de upgrade para plano PRO          |
| `{{hora_atual}}`     | Timestamp formatado localmente                   |

---

## 4. Categorias de Modelos

### 4.1 Onboarding Assistido (sem formulário)

Objetivo: Capturar informações cruciais sem expor o usuário a processos tradicionais de cadastro.

**Exemplo (sem marcação casual):**
```

Para oferecer recomendações mais precisas, por favor informe:
👉 Qual é a sua área de atuação profissional atualmente?

```

---

### 4.2 Respostas Técnicas – Agente Especializado

**Exemplo para área de assistência técnica:**
```

Com base no seu segmento, sugiro o seguinte modelo de orçamento técnico:
• Diagnóstico: {{descricao\_diagnostico}}
• Valor estimado: R\$ {{valor}}
Deseja que eu gere uma versão PDF pronta para envio ao cliente?

```

---

### 4.3 Aviso de Fim de Trial

Objetivo: Comunicar de forma profissional a limitação do uso gratuito e oferecer caminho de upgrade.

```

Sua utilização atingiu o limite previsto para o modo demonstração.
Para continuar com acesso total e agentes especializados, acesse:
🔗 {{link\_upgrade}}

```

---

### 4.4 Gatilhos de Conversão PRO

Objetivo: Levar o usuário a contratar de forma natural e racional, com CTA elegante.

```

Pronto. A partir deste ponto, agentes personalizados são liberados somente para usuários PRO.
Deseja ativar agora e liberar recursos completos?
👉 [Ativar Plano PRO]({{link_upgrade}})

```

---

### 4.5 Respostas Neutras para Venda (Assistente de Copy)

Objetivo: Gerar respostas personalizadas com foco em engajamento de leads dos clientes.

```

Sugestão de resposta profissional para o seu cliente:
"Olá! Trabalho com {{servico}} e posso te ajudar com qualidade e agilidade. Deseja um orçamento rápido por aqui mesmo?"
Quer que eu prepare outras variações mais persuasivas?

```

---

## 5. Compliance e Restrições

Todas as respostas devem obedecer às políticas da Meta mesmo em ambiente Z-API não oficial:

- Proibido qualquer forma de spam ou envio em massa automatizado;
- Proibido solicitações explícitas de dados sensíveis via WhatsApp;
- Restrições de linguagem: nenhuma resposta pode conter expressões sensacionalistas, discriminatórias ou que estimulem comportamento irregular.

Mensagens que violarem regras de compliance devem ser automaticamente reescritas ou bloqueadas pelo **Agente Fiscal**.

---

## 6. Versionamento e Evolução

Este documento é versionado em repositório Git e sua modificação depende de aprovação técnica da equipe de arquitetura. Todos os modelos devem ser auditáveis e passíveis de rollback.

---

## 7. Referências Internas

- [agente-fiscal](../../agente-fiscal/)
- [orquestrador](../../orquestrador/)
- [ROMs por profissão - docs/modelos/roms_profissionais/]

---
