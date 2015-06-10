import bs4
import requests
response = requests.get('http://www.fda.gov/ICECI/Inspections/ucm381526.htm#foods')
soup = bs4.BeautifulSoup(response.text)

table = soup.select('table')[1]
row = table.select('tr')[1]

col = row.select('td')[3]
print(col.text)