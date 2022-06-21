# 37 В матрице найти среднее арифметическое элементов последних двух столбцов.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица: ")
for i in matrix:
    print(i)

summa = 0
for i in matrix:
    summa += i[-1] + i[-2]
print("Среднее арифметическое:", summa / (len(matrix) * 2))
