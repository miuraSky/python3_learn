from collections import deque

queue = deque(['Eric', 'John', 'Micheal'])
queue.append('Terry')
queue.append('Graham')

print(1, queue)
print(2, queue.popleft())
print(3, queue.popleft())
print(4, queue)
