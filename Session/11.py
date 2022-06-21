# 11 В матрице элементы первого столбца возвести в куб.
from random import randint

x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(-2, 2) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

for i in matrix:
    i[0] = i[0] * i[0] * i[0]

print('Полученная матрица:')
for i in matrix:
    print(i)
