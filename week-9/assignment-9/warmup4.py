import requests
url = "https://thisurldoesnotexist.example.com"
try:
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Could not reach the server. Check your connection and try again.")
    else:
        data = response.json()
except requests.exceptions.RequestException:
    print("Error: Could not reach the server. Check your connection and try again.")