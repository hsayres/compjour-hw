import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json'
data = json.loads(requests.get(data_url).text)

print('A. ', data['created_at'])
print('B. ', data['user']['created_at'])
print('C. ', data['text'])
print('D. ', data['user']['screen_name'])
print('E. ', data['id'])
print('F. ', len(data['entities']['user_mentions']))

hashtag_objs = data['entities']['hashtags']
hashtag_texts = []
for h in hashtag_objs:
	hashtag_texts.append(h['text'])

print('G. ', ', '.join(hashtag_texts))

URL_objs = data['entities']['urls']
URL_texts = []
for u in URL_objs:
	URL_texts.append(u['display_url'])

print('H. ', ', '.join(URL_texts))