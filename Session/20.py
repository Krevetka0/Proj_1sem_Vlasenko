# 20 В матрице найти среднее арифметическое положительных элементов.
from random import randint
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = [[randint(-10, 10) for i in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(i)

h = []
for i in matrix:
    for o in i:
        if o > 0:
            h.append(o)
print('Среднее арифметическое положительных элементов:', round(sum(h) / len(h), 2))
