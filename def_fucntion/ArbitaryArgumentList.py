def concat(*args, sep = '/'):
    return sep.join(args)

print(concat('earth', 'mars', 'venus', '谷军宇'))
print(concat('earth', 'mars', 'venus', '谷军宇', sep = ','))

def normal_concat(sep, *args):
    return sep.join(args)

print(normal_concat('-', 'earth', 'mars', 'venus', '谷军宇'))
