import requests
import json

durl = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
data = json.loads(requests.get(durl).text)
quakes = data['features']

def get_mag(quake):
	return quake['properties']['mag']

x=0

for quake in quakes:
	if (get_mag(quake) >= 4.5):
		x+=1

print(x)
