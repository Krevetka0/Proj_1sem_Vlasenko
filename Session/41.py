# 41 В матрице найти минимальный элемент в предпоследней строке.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица:")
for i in matrix:
    print(i)
print("Минимальный элемент предпоследней строки:", min(matrix[y-2]))
