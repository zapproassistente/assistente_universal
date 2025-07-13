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
git stash pop || echo "⚠️ Nenhuma mudança local para restaurar."

PAINEL_ORIGEM="painel"
PAINEL_DESTINO="/var/www/painel"

if [ -d "$PAINEL_ORIGEM" ]; then
  echo "🧩 Atualizando painel..."
  sudo cp -r "$PAINEL_ORIGEM"/* "$PAINEL_DESTINO"/
  sudo chown -R www-data:www-data "$PAINEL_DESTINO"
  echo "✅ Painel sincronizado e atualizado!"
else
  echo "⚠️ Pasta '$PAINEL_ORIGEM' não existe. Ignorando atualização do painel."
fi
