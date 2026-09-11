import requests
import config
import argparse

API_URL = "https://api.restcountries.com/countries/v5"
API_KEY = config.api_key

def fetch_data():
    params = {
        "api_key": API_KEY,
        "fields": "name,capital,region,population,gini_coefficient,government_type"
        }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {type(e).__name__} — {e}")
        return []
        
def skipped_countries(data, region_input):
    if data == []:
        print("The list is empty.")
        return []
    else: 
        countries_not_counted = 0
        for country in data["data"]["objects"]:
            if country["region"].lower() == region_input:
                if country["economy"]["gini_coefficient"] == {}:
                    countries_not_counted += 1
        return countries_not_counted
       
def process_data(data, region_input):
    if data == []:
        print("The list is empty.")
        return []
    else:
        cleaned = []
        for country in data["data"]["objects"]:
            gini_coefficients = []
            if country["region"].lower() == region_input:
                if country["economy"]["gini_coefficient"] == {}:
                    gini_coefficients.append({
                        "year": "N/A",
                        "gini_coefficient": "N/A"
                    })
                else:
                    for year, gini in country["economy"]["gini_coefficient"].items():
                        gini_coefficients.append({
                            "year": int(year),
                            "gini_coefficient": float(gini)
                        })
                    cleaned.append({
                        "name": country["names"]["common"],
                        "capital": country["capitals"][0]["name"] if country.get("capitals") and country["capitals"][0]["attributes"].get("primary") else "N/A",
                        "region": country["region"],
                        "population": country["population"],
                        "government_type": country["government_type"],
                        "gini_coefficients": gini_coefficients,
                        "number_of_data_points": len(country["economy"]["gini_coefficient"]),
                        "difference_between_strtend_gini_values": abs(float(gini_coefficients[0]["gini_coefficient"] - gini_coefficients[len(gini_coefficients)-1]["gini_coefficient"])),
                        "difference_between_years": int(gini_coefficients[len(gini_coefficients)-1]["year"] - gini_coefficients[0]["year"]),
                        "strt_gini": float(gini_coefficients[0]["gini_coefficient"]),
                        "end_gini": float(gini_coefficients[len(gini_coefficients)-1]["gini_coefficient"])
                    })
        return cleaned
          
def display_results(results, skipped_countries, region_input):
    if results == []:
        print("No results found from inquiry. Please try again.")
    else:
        region_list = sorted(results, key=lambda country: country["difference_between_strtend_gini_values"], reverse=True)
        print(f"\n=== Income Inequality Report — {region_input.capitalize()} ===")
        print(f"\nCountries included: {len(results)}")
        print(f"Countries skipped due to missing data: {skipped_countries}\n")
        for country in region_list:
            print(f'Country: {country["name"]}\n')
            print(f'Region: {country["region"]} | Capital: {country["capital"]} | Population: {"{:,}".format(country["population"])}')
            print(f'Government Type: {country["government_type"]}\n')
            print(f'Number of Data Points: {country["number_of_data_points"]}\n')
            for dictionary in country["gini_coefficients"]:
                print(f'Year: {dictionary["year"]} | Gini Coefficient: {dictionary["gini_coefficient"]}')
            if country["difference_between_strtend_gini_values"] > 0 and country['number_of_data_points'] > 1:
                print(f'\nSynopsis: {country["name"]} is experiencing less income inequality.\n')
                print(f'Over the course of {country["difference_between_years"]} years, inequality decreased by a margin of {abs(round(country["difference_between_strtend_gini_values"], 1))} percentage points.')
                print(f'This translates to a relative decrease of {round(abs(1 - (country["end_gini"]/country["strt_gini"])) * 100, 2)}% in inequality, according to this metric.\n')
            elif country["difference_between_strtend_gini_values"] < 0 and country['number_of_data_points'] > 1:
                print(f'\nSynopsis: {country["name"]} is experiencing more income inequality.\n')
                print(f'Over the course of {country["difference_between_years"]} years, inequality increased by a margin of {abs(round(country["difference_between_strtend_gini_values"], 1))} percentage points.')
                print(f'This translates to a relative increase of {round(abs(1 - (country["end_gini"]/country["strt_gini"])) * 100, 2)}% in inequality, according to this metric.\n')
            elif country["difference_between_strtend_gini_values"] == 0 and country['number_of_data_points'] > 1:
                print(f'\nSynopsis: {country["name"]} is experiencing the same level of income inequality.\n')
            elif country['number_of_data_points'] == 1:
                print(f'\nSince there is only 1 data point, there is not enough information to conclude any changes to income inequality.\n')

def main():
    data = fetch_data()
    if not data:
        return
    parser = argparse.ArgumentParser(description="Query country data by region.")
    parser.add_argument("region", help="The region to filter by (e.g. Europe, Oceania, Americas, Antarctic, Asia, Africa)")
    args = parser.parse_args()
    
    uncounted_countries = skipped_countries(data, args.region.lower())
    new_data = process_data(data, args.region.lower())
    
    display_results(new_data, uncounted_countries, args.region.lower())

if __name__ == "__main__":
    main()
