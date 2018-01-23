





the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")



# strings in Python
word = "Python"
print(word[0])
print(word[-1])

print(word[:2])
print(word[2:5])
print(word[:5])
print(word[-2:])
print("word length:", len(word))
# print nothing
# print(word[-2:0])

# strings is immutable

# Lists in Python
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:]) # slicing returns a new list

squaresCopy = squares[:] # copy list
print(squaresCopy)

squaresConcat = squares + [36, 49, 64, 81, 100]
print(squaresConcat)

cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

# Fibonacci 数列
a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a + b

