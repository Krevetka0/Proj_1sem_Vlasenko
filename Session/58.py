# 58 В матрице элементы третьей строки заменить элементами из одномерного массива соответствующей размерности.
from random import randint
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = [[randint(0, 10) for i in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(i)
matrix[2] = [randint(-10, 0) for o in range(n)]
print('Полученная матрица:')
for i in matrix:
    print(i)
