
import csv
import requests
CSVURL = 'https://www.federalregister.gov/articles/search.csv?conditions%5Bpublication_date%5D%5Bis%5D=06%2F08%2F2015&conditions%5Btype%5D=NOTICE'
response = requests.get(CSVURL)
f = open("pubs.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("pubs.csv"))

rows = list(data)
print(len([i for i in rows]))
