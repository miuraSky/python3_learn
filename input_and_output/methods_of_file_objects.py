f = open('entirefile')
print(f.read())
print(f.read())
f.close()

print('-----------------------------------------------------------------')
f = open('entirefile')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print('-----------------------------------------------------------------')
f = open('entirefile')
for line in f:
    print(line, end='')
f.close()

print('-----------------------------------------------------------------')
f = open('entirefile', 'r+')
print(f.write('This is a test\n'))
f.close()

print('-----------------------------------------------------------------')
f = open('entirefile', 'w')
value = ('the answer', 42)
s = str(value)
print('str(value) = ' + s)
print(f.write(s))
f.close()

print('-----------------------------------------------------------------')
f = open('bfile', 'rb+')
wlen = f.write(b'0123456789abcedf')
print(wlen)

print('> 1-current:', f.tell())
print(f.seek(5)) # Go to the 6th byte in the file
print('> 2-current:', f.tell())
print(f.read(1))

print('> 3-current:', f.tell())
print(f.seek(9, 1)) # Go to the (7 + 9)th in the file, because of f.read(1)
print('> 4-current:', f.tell())
print(f.read(1))

print('> 5-current:', f.tell())
print(f.seek(-3, 2)) # Go to the 3rd byte before the end
print('> 6-current:', f.tell())

print(f.read(1))

f.close()

