import requests

url = "https://api.agify.io/?name=michael"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Name:", data["name"] if data.get("name") else "Not available")
    print("Predicted age:", data["age"] if data.get("age") else "Not available")
    if data.get("birthday"):
        print("Birthday:", data["birthday"])
    else:
        print("Birthday:", "Not available")
except requests.exceptions.RequestException as e:
    print(f"Error has occured: {e}")