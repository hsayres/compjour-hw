import bs4
import requests
response = requests.get('https://www.congress.gov/search?q=%7B%22source%22%3A%22congrecord%22%2C%22crHouseMemberRemarks%22%3A%22Issa%2C+Darrell+E.+%5BR-CA%5D%22%7D')
soup = bs4.BeautifulSoup(response.text)

section = soup.find_all(class_="results-number")

for thing in section:
	print(thing.text[50:54])