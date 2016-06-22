import os
import time
os.system('cls') #on windows

# The double split pattern- Doing a sub split - taking the name and domain name from the line and presenting them:
fhand=open('mbox-short.txt')
emailcount=dict()
for line in fhand: 
	line = line.rstrip()
	if not line.startswith('From ') :continue
	if line =='' : continue #guardian line (checking if a line is blank)
	words = line.split()
	emails = words[1] # the email string is the second object in the list
#	for email in emails
	emailcount[emails]=emailcount.get(emails,0)+1
	bigcount = None
	bigword = None
for email,count in emailcount.items():
	if bigcount is None or count > bigcount:
		bigword = emails
		bigcount = count
print bigword, bigcount
	
