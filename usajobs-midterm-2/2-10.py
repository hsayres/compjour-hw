import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()
#OrganizationName
mydict = {}
for job in data['JobData']:
    if job['OrganizationName'] in mydict:
        mydict['OrganizationName'] += 1
    else:
        mydict['OrganizationName'] = 1

print(mydict)
        