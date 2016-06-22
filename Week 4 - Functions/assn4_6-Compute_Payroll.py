hours= raw_input('Hi, Please type the number of hours you have worked: ')
hr = float(hours)
rate= raw_input('And how much do you get paid per hour? : ')
rt = float(rate)
def computepay(h,r):
	if h<=40:
		sal=h*r
	else:
		sal=r*40 + (h-40)*(r*1.5)
	print sal
	return sal
	
computepay(hr,rt)
#    