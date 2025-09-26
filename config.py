import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

def configure_api():
    """
    Carrega as variáveis de ambiente e configura a API do Gemini.
    Deve ser chamada uma vez na inicialização do aplicativo.
    """
    # Constrói o caminho para o arquivo .env na raiz do projeto
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("A variável de ambiente GOOGLE_API_KEY não foi encontrada ou está vazia. "
                         "Verifique se o arquivo .env existe na raiz do projeto e contém a chave.")

    genai.configure(api_key=api_key)
    print("API do Gemini configurada com sucesso.") # Confirmação no console