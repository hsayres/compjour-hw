import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
series = 1410
atts = {"Series": series, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
print("There are %s job listings related to 'Librarian'." %  data['TotalJobs'])
        