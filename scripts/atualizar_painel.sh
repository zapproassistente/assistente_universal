#!/bin/bash

echo "🔄 Atualizando painel para /var/www/painel..."

# Criar diretório do painel se não existir
sudo mkdir -p /var/www/painel

# Copiar os arquivos HTML do painel
sudo cp -r /home/stree/assistente_universal/painel/* /var/www/painel/

# Corrigir permissões para o usuário do NGINX
sudo chown -R www-data:www-data /var/www/painel

# Recarregar o NGINX para aplicar mudanças
sudo systemctl reload nginx

echo "✅ Painel atualizado com sucesso em http://painel.zappro.site"
