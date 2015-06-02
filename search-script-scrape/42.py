
import bs4
import requests
import datetime
response = requests.get('http://www.supremecourt.gov/opinions/slipopinions.aspx')
soup = bs4.BeautifulSoup(response.text)


table = soup.select('table')[1]
row = table.select('tr')[1]
col = row.select('td')[4]

if (col.text == 'A'):
	print("Associate Justice Samuel A. Alito, Jr.")

if (col.text == 'AS'):
	print("Associate Justice Antonin Scalia")

if (col.text == 'B'):
	print("Associate Justice Stephen G. Breyer")

if (col.text == 'D'):
	print("Decree in Original Case")

if (col.text == 'EK'):
	print("Associate Justice Elena Kagan")

if (col.text == 'G'):
	print("Associate Justice Ruth Bader Ginsburg")

if (col.text == 'K'):
	print("Associate Justice Anthony M. Kennedy")
if (col.text == 'PC'):
	print("Unsigned Per Curiam Opinion")
if (col.text == 'R'):
	print("Chief Justice John G. Roberts, Jr.")
if (col.text == 'SS'):
	print("Associate Justice Sonia Sotomayor")
if (col.text == 'T'):
	print("Associate Justice Clarence Thomas")