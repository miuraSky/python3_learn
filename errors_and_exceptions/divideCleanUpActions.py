def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    except Exception as ex:
        print('Exception ex:', ex)
    else:
        print('result is', result)
    finally:
        print('executing finally clause')

print('----------------------------------------------------------------')
divide(2, 1)

print('----------------------------------------------------------------')
divide(2, 0)

print('----------------------------------------------------------------')
divide('2', '1')
