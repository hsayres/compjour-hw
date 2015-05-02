import requests

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
state_name = 'Alaska'
atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
AlaskaTotal = int(data['TotalJobs'])
print("%s has %s job listings." % (state_name, data['TotalJobs']))
        
state_name = 'Hawaii'
atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
HawaiiTotal = int(data['TotalJobs'])
total = HawaiiTotal+AlaskaTotal
print("%s has %s job listings." % (state_name, data['TotalJobs']))
print("Together, they have {} total job listings.".format(total))