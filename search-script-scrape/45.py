
import bs4
import requests
import datetime
response = requests.get('https://www.us-cert.gov/ncas/alerts')
soup = bs4.BeautifulSoup(response.text)


print(len(soup.find_all(class_="document_id")))