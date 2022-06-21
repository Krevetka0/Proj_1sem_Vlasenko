# 34 В матрице найти сумму первых двух строк.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица:")
for i in matrix:
    print(i)
print("Сумма первых двух строк:", sum(matrix[0])+sum(matrix[1]))
