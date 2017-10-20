def fib(n):
    result = []
    a, b = 1, 2
    while a <=n:
        result.append(a)
        a, b = b, a + b
    return result

print(fib(2000))

