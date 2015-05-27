import requests
baseurl = 'https://data.usajobs.gov/api/jobs?Country='

countries = ['China', 'South Africa', 'Tajikistan']
total =0
for c in countries:
    resp = requests.get(baseurl + c)
    data = resp.json()
    total += int(data['TotalJobs'])
    print("%s currently has %s job listings." % (c, data['TotalJobs']))
print("Together, they have {} total job listings.".format(total))