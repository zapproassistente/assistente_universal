#!/bin/bash
cd /home/stree/assistente_universal || exit
git add .
git commit -m "🚀 Atualização local - $(date +%F)"
git pull origin main --rebase
git push origin main
