fname = raw_input ("Enter file name to be examined: ") #getting the file name from the user
fhand=open(fname)
counts = dict()

for line in fhand: 
	line = line.rstrip()
	if line =='' : continue #guardian pattern (checking if a line is blank)
	words = line.split()
	if words[0] != 'From' :continue
	time = words[5]
	hours = time[0:2]
	counts[hours]=counts.get (hours,0)+1

lst = list()
for key,val in counts.items():
	lst.append((key,val)) #append the keys and values of the dictionary to the new list 
lst.sort() 

for key,val in lst:  
	print key,val 


	
#print counts

	
