# ⚙️ Scripts de Automação – ZapPRO

**Resumo:**  
Este diretório concentra todos os scripts de automação de rotina do ZapPRO: deploy de painel, sincronização de repositório, CI/CD simplificado, configuração de ambiente, atualização de landing, atalhos para painel dev e mais.

---

## **Scripts disponíveis**

- **atualizar_painel.sh**  
  Atualiza a landing/painel do ZapPRO em `/var/www/painel`, sincronizando arquivos da pasta local.  
  Uso: `bash ./scripts/atualizar_painel.sh`

- **configurar_zappro.sh**  
  Instala e configura NGINX, Certbot e certificados SSL, cria configs de domínio automaticamente para ambiente VPS.  
  Uso: `sudo bash ./scripts/configurar_zappro.sh`

- **git_pull.sh**  
  Salva mudanças locais, faz pull do GitHub, restaura o painel automaticamente.  
  Uso: `bash ./scripts/git_pull.sh`

- **git_push.sh**  
  Commit automático com data e push para main, sempre verifica branch antes.  
  Uso: `bash ./scripts/git_push.sh`

- **git_sync.sh**  
  Commita, puxa (rebase), envia pro GitHub e ainda atualiza landing page em produção (CI/CD express para landing).  
  Uso: `bash ./scripts/git_sync.sh`

- **painel_assistente.sh**  
  Menu interativo estilo terminal dev: sincronização git, deploy painel, abrir VS Code, abrir painel web — tudo sem digitar comando manual.  
  Uso: `bash ./scripts/painel_assistente.sh`

---

## **Boas práticas**

- Scripts devem ser executados da raiz do projeto, a menos que especificado.
- Sempre revise scripts antes de rodar com `sudo`.
- Nomeie novos scripts sempre explicando objetivo e passo a passo.
- Atualize este README quando adicionar script novo ou mudar algum fluxo.

---

## **Importante**

- Scripts podem (e devem) ser adaptados para cada VPS, ambiente ou domínio futuro.
- Para contribuir, sempre crie novo script ou ajuste um existente com comentários claros.
- Dúvidas ou melhorias: registre na documentação de diários dev.

---

> Atualizado em 2025-07-14  
> [Todos os direitos reservados | ZapPRO ©]
