def fibonacci(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n """
    a, b = 1, 2
    while a <= n:
        print(a, end= ' ')
        a, b = b, a + b
    print()

fibonacci(2000)
print(fibonacci(1000))

