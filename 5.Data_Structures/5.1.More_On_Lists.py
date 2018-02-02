fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
p = fruits.count('apple')
print('1', p)

p = fruits.count('tangerine')
print('2', p)

p = fruits.index('banana')
print('3', p)

p = fruits.index('banana', 4) # Find next banana starting a position 4
print('4', p)

p = fruits.reverse()
print(fruits)
print('5', p)

fruits.append('grape')
print('6', fruits)

fruits.sort()
print('7', fruits)

fruits.pop()
print(8, fruits)
