# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
import random
x = int(input('Введите размер квадратной матрицы:'))
matrix = [[random.randint(-2, 2) for i in range(x)] for j in range(x)]
print('Исходная матрица:')
for i in matrix:
    print(i)
matrix = [[matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
print('Полученная матрица:')
for i in matrix:
    print(i)
