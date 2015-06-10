
import requests
import xlrd

dls = "http://quickfacts.census.gov/cgi-bin/qfd/extract-xls?2622000"
resp = requests.get(dls)

output = open('detroit.xls', 'wb')
output.write(resp.content)
output.close()

import pandas as pd
data_xls = pd.read_excel('detroit.xls', 'Sheet1', index_col=None)
data_xls.to_csv('detroit.csv', encoding='utf-8')

import csv
data = csv.DictReader(open("detroit.csv"))
rows = list(data)
print(rows[2]['Detroit'])