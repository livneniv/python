"""
dictionaries are defined as key value pairs
defining an empty dictionary:
counts = dict()

defining a dictionary with keys and values:
DictName = {'user':1,'serial':200,'score':99}

methods for dictionaries:
print DictName.keys() # will print the keys of the dictionary
print DictName.values() # will print the values of the dictionary
print DictName.items()() # will print the full items of the dictionary


two iteration variables allow us to advance key and value iterations together (given here using the "items" method so we get both the key and it's value):
for aaa,bbb in DictName.items 
	print aaa,bbb
"""



import os
import time
os.system('cls') #on windows

"""


ddd= dict()
ddd['age']=21
ddd['course']=182
print ddd
print ddd['age']
jjj={'chuck':"1",'fred':42,'jan':100}
print jjj
print type(jjj['chuck'])


#using dictionary as counter for many items:
ccc=dict()
ccc=['csev']=1
ccc=['cwen']=1
ccc=['cwen']= ccc['cwen']+1 #adding 1 to the count of cwen


#count the apearence of a name in a list: 
#if this is the first time you encounter a name, add it to the dictionary with the value 1.
#next time you encounter the same name, just add 1 to the counter  
counts = dict()
names = ['name1','name2','name3','name4','name5','name6','name1','name2','name3','name4','name5','name6']
for name in names:
	if name not in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1
print counts


#count the apearence of a word in a text file: 
fname = raw_input ("Enter file name to be examined: ") #getting the file name from the user
fhand=open(fname)
counts = dict()

for line in fhand: 
	line = line.rstrip()
	if line =='' : continue #guardian pattern (checking if a line is blank)
	words = line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1 
print counts


"""

#count the most common word in a file:
name = raw_input("enter file name:")
handle = open(name,'r') #open file as read only
text = handle.read() #read the entire file and input it in to the 'text' variable
words= text.split()
counts=dict()
for word in words:
	counts[word]=counts.get(word,0)+1
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print bigword, bigcount
	







"""
x=list()
print type(x)
print dir(x)

#appending to a list:
stuff=list()
stuff.append('book')
stuff.append(99)
print stuff

# is something in a list? (can be used in an 'if' or  'while' statements
some=[1,2,3,4,5,6,7,8,9,10,11,12]
9 in some
15 in some
20 not in some
os.system('pause')

#sorting a list (will change the list):
friends = ['joseph','Glenn','Sally']
friends.sort()
print friends[1]

#built in functions and lists:
some=[1,2,3,4,5,6,7,8,9,10,11,12]
print len(some)
print max(some)
print min(some)
print sum(some)
print sum(some)/len(some)

os.system('pause')

#user input numbers in to a list, when 'done' is pressed, show average of numberes entered
numlist=list()
while True:
	inp=raw_input('Enter a number, when you want to calculate average, type done:')
	if inp=='done': break
	value=float(inp)
	numlist.append(value)
average=sum(numlist)/len(numlist)
print 'The numbers you have entered are:',numlist 
print 'The Average is:',average

# Splitting a string sentence in to a list of words (based on the spaces in the string)
abc='a string with five words'
list=abc.split() # if we want to split based on a diffrent character other than space we need to write it in the ()
# e.g:
#abc='a;string;with;five;words'
#list=abc.split(;)
print list
print len(list)
print list[2]


#Parsing an email log file to show on what days were the emails sent:
# a line for example looks like this: From joe.jones@joe.shmoe.com Sat Jan 5 09:12:14 2008
fhand=open('mbox-short.txt')
for line in fhand: 
	line = line.rstrip()
	if not line.startswith('From ') :continue
	words = line.split()
	print words[2] #print the second word on the list (day)
	if words==[] : continue # this is a safety check in case of a blank line so the prog won't crash 

#the same can be achieved by the following:
fhand=open('mbox-short.txt')
for line in fhand: 
	line = line.rstrip()
	if line =='' : continue #guardian pattern (checking if a line is blank)
	words = line.split()
	if words==[] : continue # this is a safety check (guardian pattern) in case of a blank line so the prog won't crash 
	if len(word) <1 :continue # this is a safety check (guardian pattern) in case of a blank line so the prog won't crash 
	if words[0] != 'From' :continue
	print words[2] #print the second word on the list (day)
	



	
# The double split pattern- Doing a sub split - taking the name and domain name from the line and presenting them:
fhand=open('mbox-short.txt')
for line in fhand: 
	line = line.rstrip()
	if not line.startswith('From ') :continue
	if line =='' : continue #guardian line (checking if a line is blank)
	words = line.split()
	email = words[1] # the email string is the second object in the list
	pieces = email.split('@') #devide the email string to two pieces - name, and domain name (division at the '@' character)
	print pieces[1] #print the second object in the list (the domain name)
	#print words[2] #print the second word on the list (day)








print range(4) 
friends = ['joseph','Glenn','Sally']
print len(friends)
print range(len(friends))

os.system('pause')

for friend in friends:
	print 'Happy New Year:', friend

#another way of doing the same thing:
	
for i in range(len(friends)):
	friend = friends[i]
	print 'Happy New Year:', friend



	
###########        This prog is searching for a "X-DSPAM-Confidence:" indicator in a file and than calculates the average of all indicatores given in the file


while True: #infinite loop (as we do not change the true state)
	fname = raw_input ("Enter file name to be examined: ") #getting the file name from the user

	os.system('cls')

	#handling edge cases
	if len(fname) <1:	#checking for empty line
		print 'invalid input'
		continue  # will go back to the begining of the "While" loop 
	try:  # Checking if opening the handle is not possible (e.g such filename does not exists)
		handle1 = open(fname)
		break # the 'try' did not crash, and so "break" will take us out of the "while" loop to continue the rest of the code
	except:
		print "No Such File"
		continue # will go back to the begining of the loop

# con:
count=-1
count=count+1
sum=0
for line in handle1:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	count=count+1
	
	float
	print "Dspam confidence is:",line[20:26]
	templine=float(line[20:26])
	sum=sum+templine
	
#print "count is:",count
#print "sum is",sum
os.system('cls')
print "Average spam confidence:",sum/count





#filecontent=handle1.read #reading the file in to a variable

# i need to check if a line contains the string: "X-DSPAM-Confidence: " and than collect string from charachter 20 to 26 (not including)

#X-DSPAM-Confidence: 0.8475

#for line in handle1:
#	line=line.rstrip() #clearing newlines from the text file, as the 'print' command refers to each line in the file as an iteration and automaticaly creates a newline
#	print line.upper() #converts each line to uppercase
"""

