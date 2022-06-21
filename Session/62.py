# 62 В матрице элементы второго столбца заменить элементами из одномерного массива соответствующей размерности.
from random import randint

x, y = int(input("Введите число строк матрицы: ")), int(input("Введите число столбцов матрицы: "))

matrix = [[randint(0, 10) for j in range(y)] for i in range(x)]
list1 = [randint(-10, 0) for x in range(x)]
print('Список для обновления матрицы', list1)
print('Исходная матрица')
for i in matrix:
    print(i)

for i in range(x):
    matrix[i][1] = list1[i]

print('Обновленная матрица')
for i in matrix:
    print(i)
