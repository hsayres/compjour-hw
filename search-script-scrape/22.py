
import bs4
import requests
response = requests.get('https://www.govtrack.us/congress/members/barbara_boxer/300011')
soup = bs4.BeautifulSoup(response.text)
section = soup.find(id="membership")

for com in section.find_all('a'):
    print(com.text)