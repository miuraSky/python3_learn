def this_fails():
    x = 1/0

import sys

try:
    this_fails()
except:
    print('Handling run-time error:', sys.exc_info()[0])
