#!/bin/bash

echo "🔄 Atualizando painel para /var/www/painel..."

sudo mkdir -p /var/www/painel

# Sincroniza, remove arquivos antigos
sudo rsync -av --delete /home/stree/assistente_universal/painel/ /var/www/painel/

# (Opcional) Permissões
sudo chown -R www-data:www-data /var/www/painel

sudo systemctl reload nginx

echo "✅ Painel atualizado com sucesso em https://painel.zappro.site"
