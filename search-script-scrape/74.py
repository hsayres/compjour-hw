import bs4
import requests
response = requests.get('http://gov.georgia.gov/bills-signed/2015')
soup = bs4.BeautifulSoup(response.text)

table = soup.select('table')[0]
row = table.select('tr')[1]
col = row.select('td')[1]
desc = col.select('a')[0]
print(desc.text)