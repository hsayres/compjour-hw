import bs4
import requests
response = requests.get('https://projects.propublica.org/nonprofits/search?c_code%5Bid%5D=&ntee%5Bid%5D=&order=revenue&q=&sort_order=desc&state%5Bid%5D=&utf8=%E2%9C%93')
soup = bs4.BeautifulSoup(response.text)
row = soup.select("tr")[1]
col = row.select("td")[0]
title = col.select("a")[0]
print(title.text)

