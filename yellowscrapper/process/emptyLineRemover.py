import csv

resultlist = []
input = open('../spiders/result.csv', 'r')
# output = open('../spiders/result_noblank.csv', 'w+')
# writer = csv.writer(output)

for row in csv.reader(input):
	if row:
		# print(row)
		resultlist.append(row)

with open('../spiders/result_noblank.csv', 'w', newline = '') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerows(resultlist)