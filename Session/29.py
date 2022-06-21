# 29 В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
from random import randint

x, y = int(input("Столбцы: ")), int(input("Строки: "))
matrix = [[randint(-10, 10) for j in range(x)] for i in range(y)]
print("Изначальная матрица: ")
for i in matrix:
    print(i)
summa = 0
summas = []
for i in range(len(matrix)):
    for e in range(len(matrix)):
        summa += matrix[e][i]
    summas.append(summa)
    summa = 0
matrix[1] = summas
print("Полученная матрица: ")
for i in matrix:
    print(i)
