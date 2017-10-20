def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

fib_name = 'fiboname'
print(__name__)

def print_name():
    print(__name__)

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
