#!/bin/bash

cd /home/stree/assistente_universal || exit

echo "🔄 Salvando estado atual..."
git add .

echo "📝 Commitando com data..."
git commit -m "💾 Atualização na VPS - $(date +%F)"

echo "📥 Rebase puxando alterações do GitHub..."
git pull origin main --rebase

echo "🚀 Enviando para o GitHub..."
git push origin main

echo "✅ Sincronização completa!"
