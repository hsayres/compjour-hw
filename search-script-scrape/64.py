import bs4
import requests
response = requests.get('http://www.fda.gov/NewsEvents/MeetingsConferencesWorkshops/PastMeetingsWithFDAOfficials/ucm439318.htm')
soup = bs4.BeautifulSoup(response.text)

article = soup.find_all(class_="row content")


print(len((article[0]).find_all('strong')))