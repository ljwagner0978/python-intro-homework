import requests

try:
    response = requests.get("https://thisurldoesnotexist.example.com")
    response.raise_for_status()
    if response.status_code != 200:
        print("Error: Could not reach the server. Check your connection and try again.")
    else:
        data = response.json()
except requests.exceptions.RequestException:
    print("Error: Could not reach the server. Check your connection and try again.")