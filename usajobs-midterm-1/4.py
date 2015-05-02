import requests
baseurl = 'https://data.usajobs.gov/api/jobs?CountrySubdivision='
states = ['California', 'Florida', 'New York', 'Maryland']
statedict={}
for s in states:
    resp = requests.get(baseurl + s)
    data = resp.json()
    statedict[s] = int(data['TotalJobs'])
print(statedict)