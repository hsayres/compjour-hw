import bs4
import requests
import datetime
response = requests.get('https://www.law.cornell.edu/uscode/text/20')
soup = bs4.BeautifulSoup(response.text)
row = soup.select('li')[-2]
print(row.text[9:11])
