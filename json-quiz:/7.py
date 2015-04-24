import requests
import json
import time
from math import radians, cos, sin, asin, sqrt

durl = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
data = json.loads(requests.get(durl).text)
quakes = data['features']

def get_mag(quake):
	return quake['properties']['mag']

x = 0
feltTitle = ""
maxFelts = 0
for quake in quakes:
	if quake['properties']['tsunami']:
		x+=1
	if quake['properties']['felt'] > maxFelts:
		maxFelts = quake['properties']['felt'] 
		feltTitle = quake['properties']['title']

q = min(quakes, key = get_mag)

qsecs = [q['properties']['time'] / 1000 for q in quakes]
qsecs = sorted(qsecs, reverse = True)
tsec = qsecs[0] 
timeobj = time.gmtime(tsec)
qsecs = sorted(qsecs, reverse = False)
tsec2 = qsecs[0]
timeobj2 = time.gmtime(tsec2)
tobjs = [time.gmtime(s) for s in qsecs]
wdays = [s.tm_wday for s in tobjs]
tofdays = [t.tm_hour for t in tobjs]
y = [d for d in wdays if d in range(0,6)]
z = [h for h in tofdays if h in range(5,9)]

def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat /2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * asin(sqrt(a)) 
	r = 6371 # Radius of earth in kilometers.
	return c * r
def distance_from_stanford(quake):
	stanford_lng = -122.166
	stanford_lat = 37.424
	coords = quake['geometry']['coordinates']
	lng = coords[0]
	lat = coords[1]
	return haversine(lng, lat, stanford_lng, stanford_lat)

r = max(quakes, key = distance_from_stanford)

def distance_from_paris(quake):
	paris_lat = 48.8567
	paris_lng = 2.3508
	coords = quake['geometry']['coordinates']
	lng = coords[0]
	lat = coords[1]
	return haversine(lng, lat, paris_lng, paris_lat)
p = max(quakes, key = distance_from_paris)

basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'
markers_str = 'markers=color:orange'
markers_str2 = 'markers=color:orange'
markers_str3 = 'markers=color:red'
for q in quakes:
	coords = q['geometry']['coordinates']
	lng = str(coords[0])
	lat = str(coords[1])
	s = '%7C' + lat + ',' + lng
	markers_str += s

for q in quakes:
	coords = q['geometry']['coordinates']
	lng = str(coords[0])
	lat = str(coords[1])
	s = '%7C' + lat + ',' + lng
	if q['properties']['mag'] <6.0:
		markers_str2 += s
	else:
		markers_str3 += s

print('A. ', data['metadata']['title'])
print('B. ', data['metadata']['count'])
print('C. ', max([q['properties']['mag'] for q in quakes]))
print('D. ', x)
print('E. ', q['properties']['title'])
print('F. ', feltTitle)
print('G. ', time.strftime('%Y-%m-%d %H:%M', timeobj))
print('H. ', time.strftime('%A, %B %d', timeobj2))
print('I. ', len(y))
print('J. ', len(z))
print('K. ', r['properties']['title'])
print('L. ', p['properties']['title'])
print('M. ', basemap_url + '&' + markers_str) 
print('N. ', basemap_url + '&' + markers_str2 + '&' + markers_str3) 

#N. Same as above, but use red markers to denote earthquakes with magnitudes 6.0 or stronger.