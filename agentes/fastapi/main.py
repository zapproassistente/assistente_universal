from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Assistente Universal API",
    version="1.0.0",
    description="Serviço FastAPI para integração com agentes do Assistente Universal"
)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API do Assistente Universal está ativa"}
