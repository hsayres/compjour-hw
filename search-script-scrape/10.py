import bs4
import requests
response = requests.get('http://transparentcalifornia.com/salaries/2010/')
soup = bs4.BeautifulSoup(response.text)
row = soup.select("tr")[1]
col = row.select("td")[1]
title = col.select("a")[0]
print(title.text)
