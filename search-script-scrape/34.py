import csv
import requests
CSVURL = 'http://www.accessdata.fda.gov/scripts/enforcement/enforce_rpt-Product-Tabs.cfm?csv'
response = requests.get(CSVURL)
f = open("product.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("product.csv"))

rows = list(data)
print(len([i for i in rows if i['Product Type'] == "Food"]))