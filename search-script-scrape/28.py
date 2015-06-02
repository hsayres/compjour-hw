import bs4
import requests
response = requests.get('https://clinicaltrials.gov/')
soup = bs4.BeautifulSoup(response.text)

line = soup.find(id="trial-count")
number = line.select('span')[0]
string = number.text
print(string[0:8])