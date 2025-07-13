#!/bin/bash

cd /home/stree/assistente_universal || {
  echo "❌ Pasta não encontrada. Abortando."
  exit 1
}

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "main" ]; then
  echo "❌ Você está na branch '$BRANCH'. Mude para 'main' antes de continuar."
  exit 1
fi

echo "📦 Preparando arquivos para commit..."
git add .

echo "📝 Tentando commitar com data..."
git commit -m "🚀 Atualização local - $(date +%F)" || echo "⚠️ Nada para commitar."

echo "📥 Sincronizando com GitHub (rebase)..."
git pull origin main --rebase

echo "🚀 Enviando alterações para o GitHub..."
git push origin main

echo "✅ Push completo!"
echo "📁 Último commit:"
git --no-pager log -1 --oneline --decorate
