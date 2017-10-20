import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OS error: {}'.format(err))
except ValueError:
    print('Could not convert data to an integer.')
except:
    print('Unexcepted error:', sys.exc_info()[0])
    raise

print('----------------------------------------------------------------')

