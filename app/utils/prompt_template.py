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
    """

def intent_user_prompt(question: str) -> str:
    return f"""
    User Question:
    {question}
    """

def answer_system_prompt() -> str:
    return """
    You are an AI assistant that answers questions about countries.

    You will be given:

    1. Country data from a reliable API
    2. The fields requested by the user

    Use ONLY the provided country data to answer.
    Do not make up information.

    If the requested field does not exist in the data, say that the information is not available.
    """

def answer_user_prompt(question: str, requested_fields, country_data) -> str:
    return f"""
    User Question:
    {question}

    Requested Fields:
    {requested_fields}

    Country Data:
    {country_data}

    Provide a clear and concise answer.
    """
