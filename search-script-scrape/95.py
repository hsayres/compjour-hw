import csv
import requests
CSVURL = 'https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD'
response = requests.get(CSVURL)
f = open("lottery.csv", "w")
f.write(response.text)
f.close()
data = csv.DictReader(open("lottery.csv"))

rows = list(data)
nums={}
for row in rows:
	string = row['Winning Numbers']
	num1 = int(float(str(string[0:2])))
	if num1 in nums:
		curr = nums[num1]
		curr += 1
		nums[num1] = curr
	else:
		nums[num1] = 1
	num2 = int(float(str(string[3:5])))
	if num2 in nums:
		curr = nums[num2]
		curr += 1
		nums[num2] = curr
	else:
		nums[num2] = 1
	num3 = int(float(str(string[6:8])))
	if num3 in nums:
		curr = nums[num3]
		curr += 1
		nums[num3] = curr
	else:
		nums[num3] = 1
	num4 = int(float(str(string[9:11])))
	if num4 in nums:
		curr = nums[num4]
		curr += 1
		nums[num4] = curr
	else:
		nums[num4] = 1
	num5= int(float(str(string[12:14])))
	if num5 in nums:
		curr = nums[num5]
		curr += 1
		nums[num5] = curr
	else:
		nums[num5] = 1
maxnum = 1
maxnumtotal = 0

for key in nums:
	if nums[key] > maxnumtotal:
		maxnum=key
		maxnumtotal=nums[key]

print(maxnum)


