# 30 В матрице найти минимальный элемент в предпоследней строке.
from random import randint
x, y = int(input("Столбцы: ")), int(input("Строки: "))
matrix = [[randint(-10, 10) for j in range(x)] for i in range(y)]
print("Изначальная матрица: ")
for i in matrix:
    print(i)
print("Минимальный элемент предпоследней строки:", min(matrix[y-2]))
