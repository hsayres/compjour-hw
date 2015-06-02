
import requests
import json
data_url = 'https://analytics.usa.gov/data/live/top-pages-realtime.json'
data = json.loads(requests.get(data_url).text)
print(data['data'][0]['page'])