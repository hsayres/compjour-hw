import requests

BASE_URL = 'https://api.fda.gov/drug/enforcement.json'
resp = requests.get(BASE_URL)
data = resp.json()
print(data)