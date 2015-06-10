import csv
import requests
CSVURL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
response = requests.get(CSVURL)
f = open("legislators.csv", "w")
f.write(response.text)
f.close()
# re-open leglislators.csv
data = csv.DictReader(open("legislators.csv"))
rows = list(data)
print(len([i for i in rows if i['gender'] == 'F' and i['in_office'] == '1']))