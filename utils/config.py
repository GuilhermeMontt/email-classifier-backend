import google.generativeai as genai
from dotenv import load_dotenv
import os

def config_gemini():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("⚠️ GOOGLE_API_KEY não encontrada no .env")

    genai.configure(
        api_key=api_key
    )

    generation_config = {
        "temperature": 0.4,
        "top_p": 0.8,
        "top_k": 40,
        "response_mime_type": "text/plain",
        "transport": "rest"
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config
    )

    return model