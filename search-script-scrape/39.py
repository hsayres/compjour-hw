
import bs4
import requests
response = requests.get('http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm384618.htm')
soup = bs4.BeautifulSoup(response.text)
section = soup.select('table')[0]
print(section.text)