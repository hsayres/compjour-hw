import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(data_url).text)
books = data['results']['books']

x=0
y=0
numWeeks = 0
mostWeeksTitle = ""
minRank = 0
minRankTitle = ""
curRank = 0
newBooks = 0
maxRank = 1000
titleMaxRank = ""
rankIncrease =0
increasetitle = ""
increaseRank = 0
rankDrop =0
dropTitle = ""
dropRank = 0
minRank = 0
s=0
t=0
u=0
titleMax=0
titleCount =0
total = 0

for book in books:
	titleCount+= len(book['title'])
	total+=1
	if book['publisher'] == "Scribner":
		x += 1
	description = book['description']
	if "detective" in description.lower():
		y +=1
	if book['weeks_on_list'] > numWeeks:
		numWeeks = book['weeks_on_list']
		mostWeeksTitle = book['title']
	if book['rank_last_week'] > minRank:
		minRank = book['rank_last_week']
		minRankTitle = book['title']
		curRank = book['rank']
	if book['rank_last_week'] == 0:
		newBooks += 1
		if book['rank'] < maxRank:
			maxRank = book['rank']
			titleMaxRank = book['title']
	if book['rank_last_week'] != 0:
		dif = book['rank_last_week']- book['rank']
		if dif <0:
			s += dif
			u += 1
		if dif > 0:
			t += dif
		if dif < rankDrop:
			rankDrop = dif
			dropTitle = book['title']
			dropRank = book['rank']
		if dif > rankIncrease:
			rankIncrease = dif
			increasetitle = book['title']
			increaseRank = book['rank']
	if len(book['title']) >titleMax:
		titleMax = len(book['title'])

seq = (mostWeeksTitle, str(numWeeks))
psv = '|'.join(seq)
seq2 = (minRankTitle, str(curRank), str(minRank))
psv2 = '|'.join(seq2)
seq3 = (titleMaxRank, str(maxRank))
psv3 = '|'.join(seq3)
seq4 = (dropTitle, str(dropRank), str(rankDrop))
psv4 = '|'.join(seq4)
seq5 = (str(u), str(s))
psv5 = '|'.join(seq5)
seq6 = (increasetitle, str(increaseRank), str(rankIncrease))
psv6 = '|'.join(seq6)


print('A. ', x)
print('B. ', y)
print('C. ', psv)
print('D. ', psv2)
print('E. ', newBooks)
print('F. ', psv3)
print('G. ', psv6)
print('H. ', psv4)
print('I. ', t)
print('J. ', psv5)
print('K. ', titleMax)
print('L. ', round(titleCount/total, 0))





