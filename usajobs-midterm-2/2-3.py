import json
with open("data-hold/domestic-jobcount.json") as f:
	domestic_data = json.loads(f.read())
with open("data-hold/intl-jobcount.json") as f:
	intl_data = json.loads(f.read())

icount = 0
for d in intl_data:
	icount += d[1]
print("There are %d international jobs." % icount)

dcount = sum([d[1] for d in domestic_data])
print("There are %d domestic jobs." % dcount)
