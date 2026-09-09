import requests

response = requests.get("https://api.agify.io/?name=michael")
print(f"Status code: {response.status_code}")
data = response.json()
print(f"Response: {data}")