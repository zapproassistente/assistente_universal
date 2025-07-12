FROM python:3.11-slim

# Evita problemas com input interativo
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copia apenas requirements primeiro para usar cache
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Porta padrão da FastAPI
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
