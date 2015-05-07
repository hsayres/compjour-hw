import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

mylist=[]
for d in domestic_data:
	if d[1] < 100:
		mylist.append([d[0], d[1]])
sortedlist = sorted(mylist)
for item in sortedlist:
	namestring = item[0]+","+str(item[1])
	print(namestring)