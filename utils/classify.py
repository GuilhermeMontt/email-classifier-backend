def classify_email(model, text: str) -> str:
    prompt = f"""
    Classifique o seguinte email como "Produtivo" ou "Improdutivo".

    Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema, horário de funcionamento, etc).
    Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).

    Atualmente não estamos em busca de contratar nimguém.

    Atenção: Retorne Apenas ""Produtivo"" ou ""Improdutivo"", sem qualquer justificativa.

    Email:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
