def generate_response(model, text: str, category: str) -> str:
    prompt = f"""
    Email classificado como: {category}

    Texto do email:
    {text}

    Gere uma resposta automática adequada:
    - Se for Produtivo, responda de forma profissional e útil.
    - Se for Improdutivo, apenas agradeça educadamente.
    """
    response = model.generate_content(prompt)
    return response.text.strip()
