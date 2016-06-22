import os
import time
os.system('cls') #on windows
	
###########        This prog is converting lower case text to uppercase	


while True: #infinite loop (as we do not change the true state)
	fname = raw_input ("Enter file name to be shouted: ") #getting the file name from the user

	os.system('cls')

	#handling edge cases
	if len(fname) <1:	#checking for empty line
		print 'invalid input'
		continue  # will go back to the begining of the "While" loop 
	try:  # Checking if opening the handle is not possible (e.g such filename does not exists)
		handle1 = open(fname)
		break # the 'try' did not crash, and so "break" will take us out of the "while" loop to convert the text
	except:
		print "No Such File"
		continue # will go back to the begining of the loop

# converting the text:

for line in handle1:
	line=line.rstrip() #clearing newlines from the text file, as the 'print' command refers to each line in the file as an iteration and automaticaly creates a newline
	print line.upper() #converts each line to uppercase

