largest=None
smallest=None
while True: #infinite loop (as we do not change the true state)
	inp= raw_input('Enter a number: ')
	
	#handling edge cases
	if inp=='done' : break
	if len(inp) <1:break #checking for empty line
	
	#doing the work
	try: #handeling string inputs
		num=float(inp)
	except:
		print "Invalid input"
		continue # will go back to the begining of the loop
	if smallest is None:
		smallest = inp
	elif inp<smallest:
		smallest=inp
	if largest is None:
		largest = inp
	elif inp>largest:
		largest=inp
	
	
print 'Maximum is ', largest
print 'Minimum is ', smallest





