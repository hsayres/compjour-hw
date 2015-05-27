import requests
import json
data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
response=requests.get(data_url)
text = response.text
data = json.loads(text)

result_obj = data['artists'][0]

print('A. ', len(data['artists']))
print('B. ', data['artists'][4]['name'])
print('C. ', data['artists'][11]['followers']['total'])

seq = (data['artists'][0]['genres'])
print('D. ', ', '.join(seq))
print('E. ', data['artists'][-1]['images'][0]['url'])