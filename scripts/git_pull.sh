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

echo "✅ Pull finalizado com sucesso! Projeto sincronizado com o GitHub."
