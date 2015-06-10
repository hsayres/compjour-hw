import bs4
import requests
import datetime
response = requests.get('http://www.gao.gov/browse/topic/Veterans')
soup = bs4.BeautifulSoup(response.text)

table = soup.select('table')[0]

section = soup.find_all(class_="scannableTitle")
for item in section:
	text = item.text
	print(text[20:26])