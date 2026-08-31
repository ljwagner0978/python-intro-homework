import requests

url = "https://api.agify.io/?name=michael"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    name = data["name"] if data.get("name") else "Not available"
    age = data["age"] if data.get("age") else "Not available"
    birthday = data["birthday"] if data.get("birthday") else "Not available"
    print("Name:", name)
    print("Predicted age:", age)
    print("Birthday:", birthday)
except requests.exceptions.RequestException as e:
    print(f"Error has occured: {e}")