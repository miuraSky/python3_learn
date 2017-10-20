s = 'Hello, world'

print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is '  + repr(y) + '...'

print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world \n'
print(hello)
print(repr(hello))

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))


print('------------------------------------------------------------')

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end = ' ')
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('------------------------------------------------------------')
a = '12'.zfill(5)
b = '-3.14'.zfill(7)
c ='3.14159265359'.zfill(5)

print(a, b, c)

print('------------------------------------------------------------')

print('We are the {} who say {}!'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'egges'))
print('{1} and {0}'.format('spam', 'egges'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

print('------------------------------------------------------------')
import math
print('The value of PI is approximately {0:.48f}.'.format(math.pi))

print('------------------------------------------------------------')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print('{0:10} ==> {1:10d}.'.format(name, phone))

print('Jack: {0[Jack]:d}; Sjored: {0[Sjoerd]:d};' 'Dcab: {0[Dcab]:d}.'.format(table))
