fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand=open(fname)
count = 0

for line in fhand: 
	line = line.rstrip()
	if line =='' : continue #guardian pattern (checking if a line is blank)
	words = line.split()
	if words==[] : continue # this is a safety check (guardian pattern) in case of a blank line so the prog won't crash 
	if len(words) <1 :continue # this is a safety check (guardian pattern) in case of a blank line so the prog won't crash 
	if words[0] == 'From':
		print words[1] #print the second word on the list (email address)
		count=count+1
print "There were", count, "lines in the file with From as the first word"

