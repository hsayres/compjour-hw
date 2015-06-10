import bs4
import requests
import datetime
response = requests.get('http://www.outragegis.com/weather/grsm/')
soup = bs4.BeautifulSoup(response.text)

text = soup.find_all(class_="feed")
humiditysec = (text[1]).text
print(humiditysec[63:66])