while True:
    try:
        x = int(input('Please enter a number:'))
        print('x * x = ', x ** 2)
        break
    except ValueError:
        print('Oops! That was no valid number. Try again...')

print('Nothing here!')

