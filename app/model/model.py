from pydantic import BaseModel
from typing import Optional, List, Dict

class CountryBase(BaseModel):
    name: str
    capital: Optional[str] = None
    population: Optional[int] = None
    currency: Optional[str] = None
    region: Optional[str] = None
    area: Optional[float] = None
    borders: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    independent: Optional[bool] = None
    un_member: Optional[bool] = None
    flag_description: Optional[str] = None
    gini: Optional[float] = None
    raw_data: Optional[Dict] = None


class CountryDataParser(CountryBase):
    
    @staticmethod
    def select_country(country_name: str, api_response: List[Dict]) -> Dict:
        """
        Select the correct country from the API response.
        Prefer exact match on name.common.
        """

        for country in api_response:
            common_name = country.get("name", {}).get("common", "")
            if common_name.lower() == country_name.lower():
                return country

        # fallback if no exact match
        return api_response[0]

    @classmethod
    def from_api_response(cls, country_name: str, api_response: List[Dict]):
        """
        Extract fields from the selected country and validate.
        """

        selected_country = cls.select_country(country_name, api_response)

        currencies = selected_country.get("currencies")
        currency_code = None
        if currencies:
            currency_code = list(currencies.keys())[0]

        languages = selected_country.get("languages")
        language_list = None
        if languages:
            language_list = list(languages.values())

        gini_value = None
        gini_data = selected_country.get("gini")
        if gini_data:
            gini_value = list(gini_data.values())[0]

        normalized_data = {
            "name": selected_country.get("name", {}).get("common"),
            "capital": (
                selected_country.get("capital")[0]
                if selected_country.get("capital")
                else None
            ),
            "population": selected_country.get("population"),
            "currency": currency_code,
            "region": selected_country.get("region"),
            "area": selected_country.get("area"),
            "borders": selected_country.get("borders"),
            "languages": language_list,
            "independent": selected_country.get("independent"),
            "un_member": selected_country.get("unMember"),
            "flag_description": selected_country.get("flags", {}).get("alt"),
            "gini": gini_value,
            "raw_data": selected_country,
        }

        return cls(**normalized_data)

    def to_dict(self):
        return self.model_dump()
