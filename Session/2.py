# 2 Возвести в квадрат отрицательные числа
from random import randint

x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(-3, 3) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

matrix = [[i * i if i < 0 else i for i in j] for j in matrix]
print('Полученная матрица: ')
for i in matrix:
    print(i)
