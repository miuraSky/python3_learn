lst = []
a, b = 0, 1

while b < 1000:
    lst.append(b)
    a, b = b, a + b

print(lst)
