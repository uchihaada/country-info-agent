import requests
from app.model.model import CountryDataParser
from dotenv import load_dotenv
import os
load_dotenv()
class CountryAPIError(Exception):
    pass

def fetch_country_data(country_name: str) -> dict:
    url = os.getenv("DATA_URL","https://restcountries.com/v3.1/name/{country_name}")
    url=url.format(country_name=country_name)
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        raise CountryAPIError(f"API request failed: {str(e)}")

    if response.status_code != 200:
        raise CountryAPIError(f"Country '{country_name}' not found")

    api_response = response.json()

    if not api_response:
        raise CountryAPIError("No country data returned")

    # Use the parser to extract and validate data
    country_obj = CountryDataParser.from_api_response(country_name, api_response)

    # Convert to dictionary
    return country_obj
