
file = open('text.txt')

for line in file:
    print(line, end='')
    
input = open('text.txt','r')
output = open('new.txt','w')

for line in input:
    print(line, file=output, end='')


#Write to another file
buffersize = 10
infile = open('text.txt','r')
outfile = open('newbigfile.txt','w')

buffer = infile.read(buffersize)
bufferLimit = 50000

while bufferLimit > 0:
    outfile.write(buffer)
    print('.',end='')
    bufferLimit = bufferLimit - buffersize
    
    
