import csv
import requests
CSVURL = 'http://www.asias.faa.gov/pls/apex/f?p=100:93::FLOW_EXCEL_OUTPUT_R2161113456916636_en'
response = requests.get(CSVURL)
f = open("accidents.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("accidents.csv"))

rows = list(data)
print(len([i for i in rows]))
