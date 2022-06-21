# 15 В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
r = int(input('Номер столбца, который мы будем увеличивать: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрциа:")
for i in matrix:
    print(i)

for i in range(y):
    matrix[i][r-1] = matrix[i][r-1] ** 2

print('Полученная матрица:')
for i in matrix:
    print(i)
