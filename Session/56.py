# 56 В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
n = int(input("Введите номер столбца: "))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)
for i in matrix:
    i[n - 1] = i[n - 1] * 2
print("Полученная матрица: ")
for i in matrix:
    print(i)
    