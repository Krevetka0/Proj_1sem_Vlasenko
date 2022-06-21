# 13 В матрице элементы строки N (N задать с клавиатуры) увеличить на 3
from random import randint

x, y = int(input('Столбцы: ')), int(input('Строки: '))
g = int(input("Введите номер строки, которую мы увеличим на 3: "))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)
u = []
for i in matrix[g - 1]:
    u.append(i + 3)
matrix[g - 1] = u
print('Полученная матрица:')
for i in matrix:
    print(i)
