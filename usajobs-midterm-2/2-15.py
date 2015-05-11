


import json
import requests
from operator import itemgetter

import os
with open("sample-geochart-cities.html") as f:
    htmlstr = f.read()
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
locationlist =[]
for job in jdata['jobs']:
	locationlist.append(job['Locations'])
loclist=[]
for thing in locationlist:
	loclist.extend(thing.split(';')) 

def get_ca_cities(loclist):
	xlist=[]
	for item in loclist:
		if ('California' in item):
			newlocation = item.replace(', California', '')
			xlist.append(newlocation)
	return xlist

xlist= get_ca_cities(loclist)

mydict = {}
for loc in xlist:
	if loc in mydict:
		mydict[loc] += 1
	else:
		mydict[loc] = 1
mylist = [['City', 'Jobs']]

for key in mydict:
	mylist.append([key, mydict[key]])

tablerows = []
mylist2=mylist[1:]
sorteddata = sorted(mylist2, key = itemgetter(1), reverse = True)

for d in sorteddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)

with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(mylist))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)



