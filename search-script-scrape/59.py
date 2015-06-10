import bs4
import requests
response = requests.get('http://catalog.data.gov/dataset?vocab_category_all=Higher+Education&groups=education2168&_groups_limit=0&_vocab_category_all_limit=0')
soup = bs4.BeautifulSoup(response.text)

line = soup.find(class_="new-results")
string = line.text
print(string[17:19])