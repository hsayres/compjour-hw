import bs4
import requests
response = requests.get('http://www.dallaspolice.net/ois/ois.html')
soup = bs4.BeautifulSoup(response.text)

tab = soup.select('table')[1]
rows = len(tab.find_all('tr'))-1

print(rows)