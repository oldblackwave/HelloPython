a = 50.0
print(type(a),a)

b = int(50.1)
print(type(b),b)

c = round(50.7)
print(type(c),c)

d = float(50)
print(type(d),d)

e = "Hello Ass!!"
print(type(e),e)

f = '''
    HiHi
    you
    Ass
    '''
print(type(f),f);

g = 'This is \na string'
print(g)

h = "Hello"
i = 'This is %s a string' % h
print(i)

j = 'This is {} string'.format(h)
print(j)

k = (1,2,3,4,5,6,7,8)
print(type(k),k)

l = [1,2,3,4,5,6,7,8]
l.append(9)
print(type(l),l)
print(type(l),l[2])
print(type(l),l[2:6])
print(type(l),l[:6])

m = {'one':1, 'two':2, 'three':3}
n = {'id':5, 'name':'alex'}
print(type(m),m,n)

dictionary = dict(
                  one = 1, two = 'two'
                  )
print(type(dictionary),dictionary)

boolean = True
a, b = 0,1 
if a==b:
    print(True)
else:
    print(False)
print(type(boolean),boolean)