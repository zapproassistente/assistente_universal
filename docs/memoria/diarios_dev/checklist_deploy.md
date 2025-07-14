# 📝 Checklist de Deploy – ZapPRO

**Resumo:**  
Lista prática e objetiva para revisar antes de qualquer novo deploy, atualização ou rollout em produção do ZapPRO. Reduz risco de erro, downtime, perda de dado ou impacto em cliente. Ideal para devs, ops e responsáveis por releases.

---

## **Checklist rápido pré-deploy**

- [ ] **Código revisado e testado em ambiente local/dev**
- [ ] **Integração WhatsApp (Z-API) validada e respondendo**
- [ ] **Variáveis .env revisadas** (token ZAPI, OpenAI, endpoints, etc)
- [ ] **docker-compose.yml atualizado** (novos serviços, versões, portas)
- [ ] **Backup do banco de dados realizado**
- [ ] **Scripts de automação revisados** (git_sync.sh, painéis, etc)
- [ ] **Agente Fiscal ativo e validando respostas**
- [ ] **Testes manuais no WhatsApp com usuário de sandbox**
- [ ] **Logs limpos de erros críticos**
- [ ] **Monitoramento/configuração de alertas habilitado**
- [ ] **Certificados SSL e domínios OK (landing, painel, API)**
- [ ] **README do deploy revisado**

---

## **Checklist pós-deploy**

- [ ] **Acesso imediato ao sistema: landing page, painel e APIs**
- [ ] **Logs de deploy registrados**
- [ ] **Verificar uso de memória e CPU dos containers**
- [ ] **Validação das rotas principais de cada agente**
- [ ] **Envio de mensagem teste via WhatsApp (entrada/saída)**
- [ ] **Confirmar limites e bloqueios ativos**
- [ ] **Monitoramento de erros habilitado**
- [ ] **Confirmação de recebimento do serviço pelo cliente/admin**

---

## **Em caso de erro/downtime**

- [ ] **Executar rollback do container/banco**
- [ ] **Restaurar backup realizado antes do deploy**
- [ ] **Registrar causa do erro em incidentes.md**
- [ ] **Notificar admin/time e clientes afetados**

---

## **Dica extra**

> Sempre faça deploys em horários de menor uso (madrugada ou fim de semana) e avise clientes estratégicos com antecedência.

---

> Atualizado em 2025-07-14  
> [Todos os direitos reservados | ZapPRO ©]
