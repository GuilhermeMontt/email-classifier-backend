from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.file_handler import read_txt, read_pdf
from utils.preprocess import clean_text
from utils.classify import classify_email
from utils.response import generate_response
import os


app = FastAPI(title="Email Classifier API", version="1.0")


# Adicionar o middleware de CORS para permitir a comunicação
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.get("/")
async def debug():
    api_key = os.getenv("GOOGLE_API_KEY")

    return {"resposta": api_key}

@app.post("/process-email")
async def process_email(
    file: UploadFile | None = None,
    text: str | None = Form(None)
):
    content = ""

    if file:
        if file.filename.endswith(".txt"):
            content = await read_txt(file)
        elif file.filename.endswith(".pdf"):
            content = await read_pdf(file)
        else:
            raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado")

    elif text:
        content = text

    if not content:
        raise HTTPException(status_code=400, detail="Mensagem vazia")

    
    cleaned = clean_text(content)
    category = classify_email(cleaned)
    response = generate_response(cleaned, category)

    return {
        "categoria": category,
        "resposta": response
    }
