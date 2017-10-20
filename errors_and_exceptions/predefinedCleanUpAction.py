
try:
    f = open('myfile');
except:
    print('except')
else:
    for line in f:
        print(line, end='')
