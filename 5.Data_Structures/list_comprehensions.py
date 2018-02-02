gquares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
print(x)

squares = [x ** 2 for x in range(20)]
print(squares)

compre_list = list(range(10))
print(compre_list)

print('-------------------------------------------------')

listTupleXY = [(x, y) for x in [1, 2 ,3] for y in (3, 1, 4) if x != y]
print(listTupleXY)

vec = [-4, -2, 0, 2, 4]
print([x ** 2 for x in vec])
print([x ** 2 for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruits = ['  banana', ' loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruits])

print([(x, x ** 2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

vecList = []
for elem in vec:
    for num in elem:
        vecList.append(num)

print(vecList)

# list comprehensions can contain complex expressions and nested functions
from math import pi
print([str(round(pi, i)) for i in range(6)])

