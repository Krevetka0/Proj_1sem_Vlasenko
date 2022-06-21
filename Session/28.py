# 28 В матрице найти минимальный элемент в предпоследнем столбце.
from random import randint
x, y = int(input("Столбцы: ")), int(input("Строки: "))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Изначальная матрица: ")
for i in matrix:
    print(i)
wew = [matrix[i][x-2] for i in range(len(matrix))]
print('Минимальный элемент предпоследнего столбца: ', min(wew))
