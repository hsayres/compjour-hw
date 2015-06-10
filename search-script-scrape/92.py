import csv
import requests
CSVURL = 'http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/2012Q4-detail.csv'
response = requests.get(CSVURL)
f = open("payouts.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("payouts.csv"))

rows = list(data)
total = 0

for row in rows:
	if ((row['OFFICE'] == 'HON. AARON SCHOCK') and (row['RECIP (orig.)'] == 'LOBAIR LLC')):
		total += int(float(str(row['AMOUNT'])))

print(total)