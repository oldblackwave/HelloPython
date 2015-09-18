import datetime
import sys
import os

start = datetime.datetime.now()

#print(now)

i = 0
while i < 1000000:
    i = i + 1
    
end = datetime.datetime.now()

print(end - start)


print(sys.path)
print(os.name)

