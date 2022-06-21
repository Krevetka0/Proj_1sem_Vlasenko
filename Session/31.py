# 31 В матрице найти суммы элементов каждой строки и поместить их в
# новый массив. Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы
from random import randint

x, y = int(input("Столбцы: ")), int(input("Строки: "))
matrix = [[randint(-10, 10) for j in range(x)] for i in range(y)]
print("Изначальная матрица: ")
for i in matrix:
    print(i)
summa = 0
summas = []
for i in range(len(matrix)):
    for e in matrix[i]:
        summa += e
    matrix[i][2] = summa
    summa = 0
print("Полученная матрица: ")
for i in matrix:
    print(i)
