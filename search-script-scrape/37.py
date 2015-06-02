import bs4
import requests
response = requests.get('https://www.cia.gov/about-cia/leadership')
soup = bs4.BeautifulSoup(response.text)
section = soup.find_all(class_="documentByLine")
for item in section:
	div = item.select('div')[2]
	text = div.text
	print(text[20:])

