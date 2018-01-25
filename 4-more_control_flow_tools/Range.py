# 1.range()返回iterable对象
# 2. iterable对象不会实时创建list，降低GC压力
a = ['Mary', 'had', 'a', 'little', 'lamb']
print(range(len(a)))
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))
