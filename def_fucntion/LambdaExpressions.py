def make_incrementor(n):
    return lambda x: x + n

func = make_incrementor(42)
print(func(0))
print(func(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)

pairs.sort(key = lambda pair: pair[1])
print(pairs)
