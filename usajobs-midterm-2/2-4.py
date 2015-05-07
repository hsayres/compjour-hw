import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

# using standard for loop
#dcount = 0
#for d in intl_data:
#    dcount += d[1]
#print("There are %s international jobs." % dcount)