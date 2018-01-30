def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(40)
print(f(9))
print(f(7))

pairs = [(1, 'one', 4), (2, 'two', 3), (3, 'three', 2), (4, 'four', 1)];
print(pairs)

pairs.sort(key=lambda pair : pair[0])
print(pairs)

pairs.sort(key=lambda pair : pair[1])
print(pairs)

pairs.sort(key=lambda pair : pair[2])
print(pairs)
