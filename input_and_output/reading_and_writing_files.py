f = open('workfile')
print(f.closed)

with open('workfile') as fo:
    print(fo.read())
print(fo.closed)

