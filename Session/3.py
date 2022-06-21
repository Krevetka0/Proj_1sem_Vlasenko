# 3 В матрице найти минимальный и максимальный элементы.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
mat = [[randint(-10, 10) for i in range(x)] for j in range(y)]
print("Исходная матрица: ")
for i in mat:
    print(i)
up = [max(i) for i in mat]
down = [min(i) for i in mat]
print("Максимальный элемент матрицы:", max(up), "\nМинимальный элемент матрицы:", min(down))
