basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

if 'orange' in basket:
    print('orange in basket')
else:
    basket.append('orange')

if 'crabgrass' in basket:
    print('crabgrass in basket')
else:
    basket.add('crabgrass')

print(basket)

# Demostrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

set_comprehensions = {x for x in 'abracadabra' if x not in 'abc'}
print(set_comprehensions)
