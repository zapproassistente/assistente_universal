#!/bin/bash

cd /home/stree/assistente_universal || {
  echo "❌ Pasta não encontrada! Abortando."
  exit 1
}

echo "🔄 Salvando estado atual..."
git add .

echo "📝 Tentando criar commit com data e hora..."
COMMIT_MSG="💾 Atualização na VPS - $(date '+%Y-%m-%d %H:%M:%S')"

# Só tenta commitar se tiver mudanças
if git diff --cached --quiet; then
  echo "⚠️ Nenhuma mudança para commitar."
else
  git commit -m "$COMMIT_MSG"
  echo "✅ Commit realizado: $COMMIT_MSG"
fi

echo "📥 Puxando últimas alterações do GitHub com rebase..."
git pull origin main --rebase

echo "🚀 Enviando alterações para o GitHub..."
git push origin main

echo "✅ Sincronização completa com sucesso!"
