
import csv
import requests
CSVURL = 'https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv'
response = requests.get(CSVURL)
f = open("fatalities.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("fatalities.csv"))

rows = list(data)
print(len([i for i in rows if i['Date of Incident']!='']))

