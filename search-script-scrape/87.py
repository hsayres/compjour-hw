import bs4
import requests
response = requests.get('https://nfdc.faa.gov/xwiki/bin/view/NFDC/Construction+Notices')
soup = bs4.BeautifulSoup(response.text)

airports = soup.select('ul')[3]
li = airports.find_all('li')

print(len(li))