# Lists might contain items of different types, but usually the items all have the same type.
# 一种没有泛型的松散编程语言，Java中特意添加了泛型而Python却没有，但python能自成体现，其哲学？

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3])
print(squares[:])

squares += [36, 49, 64, 81, 100]
print(squares)


# lists are mutable type
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

# nest lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print('a =', len(a), ':', a)
print('n =', len(n), ':', n)
print('x =', len(x), ':', x)
