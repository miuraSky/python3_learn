def create_multipliers():
    return [lambda x, t = i: t * x for i in range(5)]

cm = create_multipliers()
print(cm)

print(cm[0](1))
print(cm[1](1))
print(cm[2](1))
print(cm[3](1))
print(cm[4](1))
