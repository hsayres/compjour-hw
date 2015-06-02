import bs4
import requests
response = requests.get('https://clinicaltrials.gov/ct2/results?term=alcohol&cond=%22Alcohol-Related+Disorders%22')
soup = bs4.BeautifulSoup(response.text)

section = soup.find_all(class_="results-summary")
for item in section:
	text = item.text
	print(text[0:3])
