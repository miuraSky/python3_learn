
matrix = [
    [1, 2, 3, 4],
    ['a', 'b', 'c', 'd'],
    ['I', 'II', 'III', 'IX'],
    ['一', '二', '三', '四']
]

print([[row[i] for row in matrix] for i in range(4)])
