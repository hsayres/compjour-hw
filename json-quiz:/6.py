import requests
import json
import os
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)


tfile.close()
accounts=json.loads(j)

print('A. ', len(accounts))

x = 0
y = 0
followerMax = 0
maxTweets = 0
followerMaxName = ""
maxTweetsName = ""
maxTweetsUnverified = 0
totalFollowers = 0
followers = []
for a in accounts:
    if a['followers_count'] > 10000:
        x += 1
    if a['followers_count'] > followerMax:
    	followerMax = a['followers_count']
    	followerMaxName = a['screen_name']
    if a['verified'] == True:
    	y += 1
    if hasattr(a, 'verified')== False:
    	if a['statuses_count'] > maxTweetsUnverified:
    		maxTweetsUnverified = a['statuses_count']
    		maxTweetsName = a['screen_name']
    if a['statuses_count'] > maxTweets:
    	maxTweets = a['statuses_count']
    totalFollowers += a['followers_count']
    followers.append(a['followers_count'])

medval = sorted(followers)[round(len(accounts)/2)-1]
print('B. ', x)
print('C. ', y)
print('D. ', followerMax)
print('E. ', maxTweets)
print('F. ', followerMaxName, 'has', followerMax, 'followers')
print('G. ', maxTweetsName, 'has', maxTweetsUnverified, 'tweets')
print('H. ', round(totalFollowers/len(accounts)))
print('I. ', medval)