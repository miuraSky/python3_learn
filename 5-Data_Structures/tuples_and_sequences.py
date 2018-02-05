# Python 的对于类型的判断要么基于声明方式、要么基于数值推断

# 单独声明元组不使用括号是有原因的
t = 12345, 54321, 'hello'
print(t[2])
print(t)

empty = ()
# 为了不让单一元素的元组看着更丑
singleton = 'hello',

print(len(empty))
print(len(singleton))
print(singleton)

