import requests
import json
data_url = "https://analytics.usa.gov/data/live/ie.json"
response = requests.get(data_url)
text = response.text
data = json.loads(text)
print(data['totals']['ie_version']['6.0'])