# 4 Найти сумму отрицательных элементов первой трети матрицы.
from random import randint
x, y = int(input('Столбцы: ')),  int(input('Строки: '))
mat = [[randint(-10, 10) for i in range(x)] for j in range(y)]
print("Исходная матрица: ")
for i in mat:
    print(i)
s = 0
for i in range(0, round(x/3)):
    for k in range(y):
        if mat[i][k] < 0:
            s += mat[i][k]
print('\nСумма отрицательных элементов 1й трети матрицы: =', s)
