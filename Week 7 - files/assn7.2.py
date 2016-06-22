import os
import time
os.system('cls') #on windows
	
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

