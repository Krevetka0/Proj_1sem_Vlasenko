# 55 Программа меняет все элементы последней строки матрицы на 0
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

for i in range(x):
    matrix[-1][i] = 0

print('Полученная матрица:')
for i in matrix:
    print(i)
