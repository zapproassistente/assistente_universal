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

echo "🌐 Atualizando landing page em /var/www/html..."
sudo mkdir -p /var/www/html
sudo cp -r html/* /var/www/html/
sudo chown -R www-data:www-data /var/www/html

echo "🔁 Reiniciando NGINX..."
sudo systemctl reload nginx

echo "✅ Sincronização e deploy concluídos!"
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

echo "🌐 Atualizando landing page em /var/www/html..."
sudo mkdir -p /var/www/html
sudo cp -r html/* /var/www/html/
sudo chown -R www-data:www-data /var/www/html

echo "🔁 Reiniciando NGINX..."
sudo systemctl reload nginx

echo "✅ Sincronização e deploy concluídos!"
