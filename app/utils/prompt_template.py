def intent_system_prompt() -> str:
    return """
    You are an AI agent that extracts structured intent from questions about countries.

    Your tasks:

    1. Identify the country mentioned.
    2. Identify which data fields the user is asking about.

    Possible fields:
    capital, population, currency, region, area, borders,
    languages, independent, un_member, flag_description, gini etc.

    Return ONLY valid JSON with keys:
    country
    requested_fields
    
    Rules:
    - If the user mentions a country but does NOT request specific fields,
    return an empty list for requested_fields.
    - Do NOT guess fields.
    - Only include fields that are explicitly requested by the user.
    """

def intent_user_prompt(question: str) -> str:
    return f"""
    User Question:
    {question}
    """

def answer_system_prompt() -> str:
    return """
    You are an AI assistant that answers questions about countries.

    You will receive country data from an API.

    Use ONLY the provided data.

    Return ONLY the final answer to the user.
    Do not mention internal fields or reasoning.
    """

def answer_user_prompt(question: str, requested_fields, country_data) -> str:
    return f"""
    User Question:
    {question}

    Country Data:
    {country_data}

    Answer the question directly using the provided country data.
    Do not mention requested fields.
    """