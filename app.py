from fastapi import FastAPI, UploadFile, Form
from utils.file_handler import read_txt, read_pdf
from utils.preprocess import clean_text
from utils.classify import classify_email
from utils.response import generate_response

app = FastAPI(title="Email Classifier API", version="1.0")

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
            return {"error": "Formato de arquivo não suportado"}

    elif text:
        content = text

    if not content:
        return {"error": "Nenhum conteúdo enviado"}

    cleaned = clean_text(content)
    category = classify_email(cleaned)
    response = generate_response(cleaned, category)

    return {
        "categoria": category,
        "resposta": response
    }
