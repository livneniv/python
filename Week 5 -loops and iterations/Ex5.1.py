count =0
total=0
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
	count = count+1
	total =total+num
	print 'Number: ',num, 'Total: ',total, 'Count: ',count

print 'Average:', total/count




#serch the explanation for  while true
