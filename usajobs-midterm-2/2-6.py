def keydef(item):
    return item[1]

import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

mylist=[]
total=0
for d in intl_data:
	if d[1] > 10:
		mylist.append([d[0], d[1]])
	else:
		total += d[1]
sortedlist = sorted(mylist, key=keydef, reverse=True)
for item in sortedlist:
	namestring = item[0]+","+str(item[1])
	print(namestring)
print("Other:", total)


