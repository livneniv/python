import os
import time
os.system('cls') #on windows
i=0
phrase = 'No, Im just in it for sharing the love around. But seriously, no, SO doesnt work that way. When I find an answer roughly the same as what I was going to say, I upvote it and sometimes expand. All the rep goes to you. Anyhow, I dont need it, Ive come to the realization I will never catch Jon Skeet and even JaredPar is pulling away now that I have to spend more time doing real work :-) '
for letter in phrase:
	print phrase[0:i]
	time.sleep(0.05)
	i=i+1
	os.system ('cls')
	

#same as what is executed with the for loop, only with a while loop
#index=0
#while index< len(phrase): #len is a built in function to show the length of an object
#	letter = phrase[index]
#	print letter
#	index = index+1
#	os.system('cls')
