import sys

print(sys.argv)

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except:
        print('open fail:', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
