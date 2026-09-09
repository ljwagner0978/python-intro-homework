import requests
import config

API_KEY = config.api_key

def fetch_european_countries():
    url = "https://api.restcountries.com/countries/v5?region=Europe"
    params = {
        "api_key": API_KEY,
        "fields": "name,capital,region,population"
        }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        countries = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    cleaned = []
    for country in countries["data"]["objects"]:
        cleaned.append({
            "name": country["names"]["common"],
            "capital": country["capitals"][0]["name"] if country.get("capitals") else "N/A",
            "region": country["region"],
            "population": country["population"]
        })
    return cleaned

def main():
    country_names = fetch_european_countries()
    if country_names != []: 
        for country in country_names[:10]:
            print(country["name"])

main()
