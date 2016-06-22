#Write a program to prompt the user for hours and rate per hour to compute gross pay

user_name=raw_input('Hi Sir, Whats your name? ')
work_hours=raw_input('and how many hours have you been working? ')
work_hours=float(work_hours) #converts type from string to float
rate=raw_input('pardon me for asking, but how much do you earn per hour? ')
rate=float(rate)
pay=(rate*work_hours)
print "Well hi there ",user_name
print "your earnings are: ",pay