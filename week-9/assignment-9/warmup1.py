import requests

response = requests.get("https://api.agify.io/?name=michael")
print("Status code: ", response.status_code)
data = response.json()
print("Response: ", data)