import requests
import config

API_KEY = config.api_key

def fetch_european_countries():
    url = "https://api.restcountries.com/countries/v5?region=Europe"
    params = {
        "api_key": API_KEY
        }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        countries = response.json()
        country_names = [col["names"]["common"] for col in countries["data"]["objects"]]
        for name in country_names[:10]:
            print(name)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

fetch_european_countries()
