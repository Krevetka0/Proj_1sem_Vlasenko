# 59 Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
from random import randint

x, y = int(input('Столбцы: ')), int(input('Строки: '))

matrix = [[randint(0, 15) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)

matrix = [[0 if i > 10 else i for i in k] for k in matrix]

print("Новая матрица:")
for i in matrix:
    print(i)
