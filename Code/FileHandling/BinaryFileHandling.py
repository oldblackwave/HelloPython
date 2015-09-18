bufferSize = 100000
input = open('rabbit.jpg','rb')
output = open('labbit.jpg','wb')
buffer = input.read(bufferSize)

while len(buffer):
    output.write(buffer)
    print('.', end='')
    buffer = input.read(bufferSize)
    

