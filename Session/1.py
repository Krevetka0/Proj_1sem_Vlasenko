# 1 Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних строках и столбцах матрицы Matr2 произвольного размера.
from numpy import *
x, y = int(input("Столбцы: ")), int(input("Строки: "))
matr2 = [[random.randint(-5, 5) for i in range(x)] for j in range(y)]
print('Исходная матрица:')
for i in matr2:
    print(i)
matr2 = delete(matr2, [0], 0)
matr2 = delete(matr2, [-1], 0)
matr2 = delete(matr2, s_[0], 1)
matr2 = delete(matr2, s_[-1], 1)
matr1 = matr2
print('Полученная матрица:')
for i in matr1:
    print(i)
