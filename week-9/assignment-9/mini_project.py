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

def country_pull():
    url = "https://api.restcountries.com/countries/v5"
    params = {
        "api_key": API_KEY,
        "fields": "name,capital,region,population"
            }
    try:
        response = requests.get(url, params=params)
        #response.raise_for_status()
        if response.status_code != 200:
            print("Error: Could not reach the server. Check your connection and try again.")
        countries = response.json()
    except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {type(e).__name__} — {e}")
            return []
    
    cleaned = []
    for country in countries["data"]["objects"]:
        cleaned.append({
            "name": country["names"]["common"],
            "capital": country["capitals"][0]["name"] if country.get("capitals") and country["capitals"][0]["attributes"].get("primary") else "N/A",
            "region": country["region"],
            "population": country["population"]
        })
    return cleaned

def country_check(search_input, countries_list):
    if countries_list == []:
        print("The list is empty.")
    else:
        custom_list = []
        for country in countries_list:
            if search_input.strip().lower() in country["name"].lower():
                custom_list.append({
                    "name": country["name"],
                    "capital": country["capital"],
                    "region": country["region"],
                    "population": country["population"],
                })
        print(f"Search: {search_input}")
        if custom_list == []:
            print("No partial or full matches, try again please.")
        else:
            for country in custom_list:
                print(f'{country["name"]} — Capital: {country["capital"]} | Region: {country["region"]} | Population: {"{:,}".format(country["population"])}')
                   
def region_check(search_input, countries_list):
    region_list = []
    for country in countries_list:
        if country["region"].lower() == search_input.strip().lower():
            region_list.append({
                "name": country["name"],
                "capital": country["capital"],
                "region": country["region"],
                "population": country["population"],
                })
            
    region_list = sorted(region_list, key=lambda country: country["population"], reverse=True)
    if(region_list == []):
        print("No results were found, try again.")
    else:
        for country in region_list:
            print(f'{country["name"]} — Capital: {country["capital"]} | Region: {country["region"]} | Population: {"{:,}".format(country["population"])}')
        
def main():
    country_list = country_pull()
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
            country_check(search_input, country_list)
            user_input = show_menu()
        elif int(user_input) == 2:
            search_input = input("Please provide a region search term (e.g. Europe, Oceania, Americas, Antarctic, Asia, Africa): ")
            while search_input.isdigit() or search_input.strip().lower() not in ["europe", "oceania", "americas", "antarctic", "asia", "africa"] :
                print("Invalid region search term inputted. Please try again")
                search_input = input("Please provide a region search term (e.g. Europe, Oceania, Americas, Antarctic, Asia, Africa): ")
            region_check(search_input, country_list)
            user_input = show_menu()
    if int(user_input) == 3:
        print("Goodbye.")
        
main()
