
import bs4
import requests
response = requests.get('http://uscode.house.gov/download/releasepoints/us/pl/113/21/usc-rp@113-21.htm')
soup = bs4.BeautifulSoup(response.text)

print(len(soup.find_all(class_="usctitlechanged"))+1)
