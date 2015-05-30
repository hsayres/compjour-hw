import csv
import requests
CSVURL = 'https://inventory.data.gov/dataset/fe9eeb10-2e90-433e-a955-5c679f682502/resource/b626ef1f-9019-41c4-91aa-5ae3f7457328/download/federalexecagncyintntdomains03302015.csv'
response = requests.get(CSVURL)
f = open("domains.csv", "w")
f.write(response.text)
f.close()
# re-open leglislators.csv
data = csv.DictReader(open("domains.csv"))

rows = list(data)
print(len([i for i in rows]))
