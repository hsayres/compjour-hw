
import bs4
import requests
import datetime
response = requests.get('http://travel.state.gov/content/passports/english/alertswarnings.html')
soup = bs4.BeautifulSoup(response.text)


print(len(soup.find_all(class_="alert"))-1)