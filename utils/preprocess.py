import re
import nltk
from nltk.corpus import stopwords
import os

# Adiciona o caminho para os dados do NLTK que serão baixados no build
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
if os.path.exists(nltk_data_path):
    nltk.data.path.append(nltk_data_path)

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)
    words = text.split()
    stop_words = set(stopwords.words("portuguese"))
    words = [w for w in words if w not in stop_words]
    return " ".join(words)
