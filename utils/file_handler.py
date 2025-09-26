import PyPDF2
from fastapi import UploadFile

async def read_txt(file: UploadFile) -> str:
    content = await file.read()
    return content.decode("utf-8")

async def read_pdf(file: UploadFile) -> str:
    reader = PyPDF2.PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
