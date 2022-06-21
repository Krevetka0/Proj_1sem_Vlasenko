# 14 В матрице элементы последнего столбца заменить на -1
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

for i in range(y):
    matrix[i][x - 1] = -1

print('Полученная матрица:')
for i in matrix:
    print(i)
