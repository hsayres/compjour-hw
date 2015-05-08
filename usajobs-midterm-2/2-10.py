import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()
#OrganizationName
mydict = {}
for job in data['JobData']:
	org = job['OrganizationName']
	if org in mydict:
		mydict[org] += 1
	else:
		mydict[org] = 1

print(mydict)
        