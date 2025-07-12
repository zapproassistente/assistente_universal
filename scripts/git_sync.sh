#!/bin/bash

cd /home/stree/assistente_universal || {
  echo "❌ Pasta não encontrada! Abortando."
  exit 1
}

echo "🔄 Salvando estado atual..."
git add .

echo "📝 Commitando com data..."
git commit -m "💾 Atualização na VPS - $(date '+%Y-%m-%d %H:%M:%S')" || {
  echo "⚠️ Nenhuma mudança para commitar."
}

echo "📥 Puxando alterações do GitHub com rebase..."
git pull origin main --rebase

echo "🚀 Enviando para o GitHub..."
git push origin main

echo "🌐 Atualizando arquivos do painel em /var/www/painel..."
cp -r /home/stree/assistente_universal/painel/* /var/www/painel/
sudo chown -R www-data:www-data /var/www/painel

echo "🔁 Reiniciando NGINX..."
sudo systemctl reload nginx

echo "✅ Sincronização e deploy concluídos!"
