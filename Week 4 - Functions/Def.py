x = raw_input('Enter Some characters: ') 
big=max(x)
small=min(x)
print 'the biggest value is: ' 
print big
print 'the smallest value is: ' 
print small


def hello():
	x=5000
	while x>10:
		x=x-1
		print x
	while x<5000:
		x=x+1
		print x
#hello()



def greet(lang):
	if lang == 'es':
		return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'
print greet('en'),'Glen'
print greet('es'),'Sally'
print greet('fr'),'Nichael'


