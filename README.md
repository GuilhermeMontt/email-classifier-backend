# Classificador de Email com IA (Backend)

Este é o backend de uma aplicação que utiliza a API do Google Gemini para classificar emails e gerar respostas automáticas. A API é construída com FastAPI.

## Deploy

A aplicação está disponível e pode ser acessada através da seguinte URL:

**[https://email-classifier-backend-in7k.onrender.com](https://email-classifier-backend-in7k.onrender.com)**

A documentação interativa da API (Swagger UI) está disponível em:
**[https://email-classifier-backend-in7k.onrender.com/docs](https://email-classifier-backend-in7k.onrender.com/docs)**

---

## Funcionalidades

- **Classificação de Emails**: Classifica o conteúdo de um email como "Produtivo" ou "Improdutivo".
- **Geração de Resposta**: Gera uma resposta automática adequada com base na classificação do email.
- **Múltiplos Formatos de Entrada**: Aceita tanto texto puro quanto arquivos nos formatos `.txt` e `.pdf`.

## Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**: Framework web para construção da API.
- **Google Gemini**: Modelo de IA para classificação e geração de texto.
- **PyPDF2**: Para extração de texto de arquivos PDF.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

---

## Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### 1. Pré-requisitos

- **Python 3.10 ou superior** instalado.
- **Git** para clonar o repositório.
- Uma **chave de API do Google Gemini**. Você pode obter uma no Google AI Studio.

### 2. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/email-classifier-backend.git
cd email-classifier-backend
```
> **Nota**: Substitua `https://github.com/seu-usuario/email-classifier-backend.git` pela URL real do seu repositório.

### 3. Crie e Ative um Ambiente Virtual

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as Dependências

Crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:

```txt
fastapi
uvicorn[standard]
python-dotenv
google-generativeai
PyPDF2
python-multipart
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

### 5. Configure as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da API do Google.

```
GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
```

### 6. Execute a Aplicação

Com tudo configurado, inicie o servidor localmente com o Uvicorn.

```bash
uvicorn app:app --reload
```

O servidor estará rodando em `http://127.0.0.1:8000`. Você pode acessar a documentação interativa em `http://127.0.0.1:8000/docs` para testar os endpoints.