fname=raw_input("What is the file name?: ")
fhand=open(fname)
newlist=list()


for line in fhand: 
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word not in newlist:
			newlist.append(word)
newlist.sort()
print newlist
	


