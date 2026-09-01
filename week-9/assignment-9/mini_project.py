import requests
import config

API_KEY = config.api_key

def show_menu():
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Quit")
    user_input = input("Choose an option (1-3): ")
    return(user_input)

def country_check(search_input):
    url = "https://api.restcountries.com/countries/v5"
    params = {
        "api_key": API_KEY
        }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        if response.status_code != 200:
            print("Error: Could not reach the server. Check your connection and try again.")
        else:
            countries = response.json()
            country_list = []
            for country in countries["data"]["objects"]:
                if search_input.lower() in country["names"]["common"].lower():
                    country_list.append({
                    "name": country["names"]["common"],
                    "capital": country["capitals"][0]["name"] if country.get("capitals") and country["capitals"][0]["attributes"].get("primary") else "N/A",
                    "region": country["region"] if country.get("region") else "N/A",
                    "population": country["population"] if country.get("population") else "N/A"
                })
            print(f"Search: {search_input}")
            if country_list == []:
                print("No partial or full matches, try again please.")
            else:
                for country in country_list:
                    print(f'{country["name"]} — Capital: {country["capital"]} | Region: {country["region"]} | Population: {"{:,}".format(country["population"])}')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {type(e).__name__} — {e}")
                   
def region_check(search_input:str):
    url = "https://api.restcountries.com/countries/v5"
    params = {
        "api_key": API_KEY
        }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        if response.status_code != 200:
            print("Error: Could not reach the server. Check your connection and try again.")
        else:
            countries = response.json()
            country_list = []
            for country in countries["data"]["objects"]:
                if country["region"] == search_input:
                    country_list.append({
                    "name": country["names"]["common"],
                    "capital": country["capitals"][0]["name"] if country.get("capitals") and country["capitals"][0]["attributes"].get("primary") else "N/A",
                    "region": country["region"] if country.get("region") else "N/A",
                    "population": int(country["population"]) if country.get("population") else "N/A"
                    })
            country_list = sorted(country_list, key=lambda country: country["population"], reverse=True)
            if(country_list == []):
                print("No results were found, try again.")
            else:
                for country in country_list:
                    print(f'{country["name"]} — Capital: {country["capital"]} | Region: {country["region"]} | Population: {"{:,}".format(country["population"])}')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {type(e).__name__} — {e}")
        
def main():
    user_input = show_menu()
    while not user_input.isdigit() or int(user_input) <= 0 or int(user_input) >= 4:
        print("Invalid input, try again please.")
        user_input = show_menu()
    while int(user_input) != 3:
        if int(user_input) == 1:
            search_input = input("Please provide a search term: ")
            while search_input.isdigit():
                print("Invalid search term inputted. Please try again")
                search_input = input("Please provide a search term: ")
            country_check(search_input)
            user_input = show_menu()
        elif int(user_input) == 2:
            search_input = input("Please provide a region search term (e.g. Europe, Oceania, Americas, Antarctic, Asia, Africa): ")
            while search_input.isdigit() or search_input.capitalize() not in ["Europe", "Oceania", "Americas", "Antarctic", "Asia", "Africa"] :
                print("Invalid region search term inputted. Please try again")
                search_input = input("Please provide a region search term (e.g. Europe, Oceania, Americas, Antarctic, Asia, Africa): ")
            region_search_standardized = search_input.capitalize()
            region_check(region_search_standardized)
            user_input = show_menu()
    if int(user_input) == 3:
        print("Goodbye.")
        
main()     