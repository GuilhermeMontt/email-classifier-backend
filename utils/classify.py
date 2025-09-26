import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def classify_email(text: str) -> str:
    prompt = f"""
    Classifique o seguinte email como "Produtivo" ou "Improdutivo".

    Email:
    {text}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
