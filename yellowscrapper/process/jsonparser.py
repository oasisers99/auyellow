import json
import json_lines
import re
from collections import Counter

names = ''
count = 0

#read json file and how number of records
with open('../spiders/medical.json', 'r') as f:
	for item in json_lines.reader(f):
		names += item['text']
		count += 1

print('total names:', count)

#change them to lower case
names = names.lower()

#remove stopwords
stopWords = ['and', 'of', 'the', 'pty', 'ltd', 'in', 'to', 'australia', 'a', 'on', 'for']
specChars = [',', '&', '-']
for eachStop in stopWords:
	names = re.sub(r'\b' + eachStop + r'\b', ' ', names)

#remove special characters
for eachChar in specChars:
	names = re.sub(eachChar, ' ', names)


#replace all spaces with a single space
names = re.sub(' +', ' ', names)
namesList = names.split(' ')

#count words and show summary
summary = Counter(namesList)
print(summary.most_common(20))