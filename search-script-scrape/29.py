import bs4
import requests
import datetime
response = requests.get('http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html')
soup = bs4.BeautifulSoup(response.text)


table = soup.select('table')[0]
row = table.select('tr')[1]
col = row.select('td')[0]
nextdate = datetime.datetime.strptime(col.text, "%m/%d/%Y").date()
now = datetime.date.today()
dif = nextdate-now
print(dif.days)
