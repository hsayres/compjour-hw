
import bs4
import requests
response = requests.get('http://www.nyclu.org/content/stop-and-frisk-data')
soup = bs4.BeautifulSoup(response.text)
listl = soup.select('ul')[-2]
row = listl.select('li')[12]
string = row.text
print(string[188:198])
