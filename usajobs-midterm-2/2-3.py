import json
with open("data-hold/domestic-jobcount.json") as f:
	domestic_data = json.loads(f.read())
with open("data-hold/intl-jobcount.json") as f:
	intl_data = json.loads(f.read())

dcount = 0
for d in intl_data:
	dcount += d[1]
print("There are %d international jobs." % dcount)

#icount = sum(d[1] for d in domestic_data)
icount=0
for d in domestic_data:
	icount+= d[1]
print("There are %d domestic jobs." % icount)
