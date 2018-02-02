from collections import deque
queue = deque(['Eric', 'John', 'Micheal'])
print(queue)
queue.append('Terry')
queue.append('Graham')
print(queue)

print(queue.pop())
print(queue)

print(queue.popleft())
print(queue)
