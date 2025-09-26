import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(text: str, category: str) -> str:
    prompt = f"""
    Email classificado como: {category}

    Texto do email:
    {text}

    Gere uma resposta automática adequada:
    - Se for Produtivo, responda de forma profissional e útil.
    - Se for Improdutivo, apenas agradeça educadamente.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
