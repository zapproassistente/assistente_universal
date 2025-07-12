#!/bin/bash

DOMAIN="zappro.site"
EMAIL="seu-email@gmail.com"  # Troque por seu email real para SSL

echo "🔧 Atualizando pacotes..."
apt update -y && apt upgrade -y

echo "📦 Instalando NGINX e Certbot..."
apt install nginx certbot python3-certbot-nginx -y

echo "🔁 Criando config NGINX para $DOMAIN..."

cat > /etc/nginx/sites-available/$DOMAIN <<EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

ln -s /etc/nginx/sites-available/$DOMAIN /etc/nginx/sites-enabled/

echo "🔍 Testando configuração NGINX..."
nginx -t

echo "🔄 Reiniciando NGINX..."
systemctl restart nginx

echo "🔐 Solicitando certificado SSL para $DOMAIN..."
certbot --nginx -d $DOMAIN -d www.$DOMAIN --email $EMAIL --agree-tos --redirect --non-interactive

echo "✅ Tudo pronto! Acesse https://$DOMAIN"
