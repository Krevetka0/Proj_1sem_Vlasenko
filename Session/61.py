# 61 сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
from random import randint

x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(1, 6) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

zero = [i if i % 2 == 0 else 0 for i in range(len(matrix))]

for i in matrix:
    for k in zero:
        i[k] = 0

print('Полученная матрица:')
for i in matrix:
    print(i)
