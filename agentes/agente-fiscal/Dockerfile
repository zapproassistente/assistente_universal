FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Instala dependências de sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos de dependências
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos da aplicação
COPY . .

# Define variável de ambiente para produção
ENV PYTHONUNBUFFERED=1

# Comando para rodar o agente fiscal
CMD ["python", "main.py"]
