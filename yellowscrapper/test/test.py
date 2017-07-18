
suburb_state = "Wind Hill Tower SA"
slist = str(suburb_state).split(' ')
size = len(slist)
suburb = ""
state = slist[size-1]
print(slist)
print(size)
if(size > 2):
    del slist[size-1]
    suburb = ' '.join(slist)
elif(size <= 2):
	suburb = slist[0]

print(state)
print(suburb)