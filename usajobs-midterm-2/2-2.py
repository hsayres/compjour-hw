import json
import os
import requests
BASE_USAJOBS_URL  = "https://data.usajobs.gov/api/jobs"
CODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
usdict = json.loads(requests.get(CODES_URL).text)

mylist = []
mylist.append(["State", "Job Count"])
for state in usdict:
	atts = {'CountrySubdivision': state, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	jobcount = int(resp.json()['TotalJobs'])
	print("Number of jobs:", jobcount)
	mylist.append([state, jobcount])

os.makedirs("data-hold", exist_ok=True)
f = open("data-hold/domestic-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()