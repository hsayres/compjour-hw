import bs4
import requests
import datetime
response = requests.get('http://www.fbi.gov/wanted/wcc/@@wanted-group-listing')
soup = bs4.BeautifulSoup(response.text)

line = soup.find(id="content")

numm= line.find_all('a')
print((len(numm)/2)+2.5)
