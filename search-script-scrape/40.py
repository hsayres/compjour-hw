
import csv
import requests
CSVURL = 'https://data.cityofchicago.org/api/views/n379-5uzu/rows.csv?accessType=DOWNLOAD'
response = requests.get(CSVURL)
f = open("requests.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("requests.csv"))

rows = list(data)
print(len([i for i in rows]))
