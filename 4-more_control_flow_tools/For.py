# 用Python则入乡随俗: 用单引号表示字符串
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, '居然还有这种操作 @_@')

# Lists在Python里面是基本类型,不然怎么这么BUG喱
print(words);
