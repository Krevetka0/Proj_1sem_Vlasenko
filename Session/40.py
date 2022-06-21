# 40 В матрице найти минимальный и максимальный элементы.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица:")
for i in matrix:
    print(i)
up = [max(i) for i in matrix]
down = [min(i) for i in matrix]
print("Максимальный элемент матрицы:", max(up), "\nМинимальный элемент матрицы:", min(down))
