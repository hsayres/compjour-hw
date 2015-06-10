


import csv
import requests
CSVURL = 'https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD'
response = requests.get(CSVURL)
f = open("whitesalaries.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("whitesalaries.csv"))

rows = list(data)
total=0
for row in rows:
	textsal = row['Salary']
	textsal= textsal[1:]
	total +=(int(float(str(textsal))))

print(total)


