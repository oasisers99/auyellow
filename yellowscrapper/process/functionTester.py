import csv
from collections import Counter

text = 'Rock and Role of king a person and Peter, and your person'
stopWords = ['and ', 'of ', 'the ', 'a ', ',']

text = text.lower()
print(text)

for eachStop in stopWords:
	text = text.replace(eachStop, '')

newList = text.split(' ')
c = Counter(newList)
print(c)


text = 'Harvey Norman,31-33 Rundle Mall, Adelaide, SA 5000'
print(text.replace(',', ' '))




# writer.writerow(resultlist)
# input.close()
# output.close()

	