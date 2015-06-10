import requests
import xlrd

dls = "http://www.tsa.gov/sites/default/files/assets/Web_Metrics/tsa.gov_customer_satisfaction_survey_october_raw_data_results_report_110114.xls"
resp = requests.get(dls)

output = open('satisfaction.xls', 'wb')
output.write(resp.content)
output.close()

import pandas as pd
data_xls = pd.read_excel('satisfaction.xls', 'Sheet1', index_col=None)
data_xls.to_csv('satisfaction.csv', encoding='utf-8')

import csv
data = csv.DictReader(open("satisfaction.csv"))
rows = list(data)
print(len([i for i in rows if i['1. How would you rate your overall experience today?'] == 'Excellent']))