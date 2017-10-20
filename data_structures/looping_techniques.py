knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
happens = ['裤子', '奶奶', '孙女']

for q, a, h in zip(questions, answers, happens):
    print('What is your {0}? It is {1}. End {2}'.format(q, a, h))

t_list = [(1, 3), ('p', 'q'), ('hello', 124)]
t_dict = {1:3, 'p': 'q', 'hello': 124}

print(t_list)
print(t_dict)
print(tuple(zip(questions, answers, happens)))
print(list(zip(questions, answers, happens)))

for x, y in t_list:
    print(x, y)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print([v for v in raw_data if not math.isnan(v)])

