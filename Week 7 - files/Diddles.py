import os
import time
os.system('cls') #on windows

fhandle = open('textfile.txt','r')
print fhandle
filename = 'textfile\n.txt'
print len(filename)
print filename
linecount=0

for line in fhandle:
	linecount=linecount+1
	print line
	time.sleep(0.05)
	os.system ('cls')

fhandle = open('textfile.txt','r')	
inp=fhandle.read() #reading the entire file in to memory
print 'The line count is:',linecount
print 'The characters count of the file is:',len(inp)

fhandle = open('textfile.txt','r')
for line in fhandle:
	line=line.rstrip()
	if line.startswith('Livne'):
		print line

fhandle = open('textfile.txt','r')
for line in fhandle:
	line=line.rstrip()
	if not 'Livne' in line:
		continue
	print line		