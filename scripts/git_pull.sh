#!/bin/bash

cd /home/stree/assistente_universal || {
  echo "❌ Pasta não encontrada! Abortando."
  exit 1
}

echo "💾 Salvando temporariamente mudanças locais (stash)..."
git stash

echo "📥 Puxando atualizações do GitHub..."
git pull origin main --rebase

echo "📂 Restaurando mudanças locais..."
git stash pop

echo "🧩 Atualizando painel (copiando para /var/www/painel)..."
sudo cp -r painel/* /var/www/painel/
sudo chown -R www-data:www-data /var/www/painel

echo "✅ Painel sincronizado e atualizado!"
