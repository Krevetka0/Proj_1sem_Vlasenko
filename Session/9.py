# 9 В матрице элементы второго столбца возвести в квадрат.
from random import randint

x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(-2, 2) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

for i in matrix:
    i[1] = i[1] * i[1]
print('Полученная матрица:')
for i in matrix:
    print(i)
