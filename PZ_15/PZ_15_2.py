#  Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
import random
x, y = [int(input(i)) for i in ('Кол-во строк:', 'Кол-во столбцов:')]
matrix = [[random.randint(-2, 2) for i in range(x)] for j in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[i][j] > 0:
            print(True)
            break
    break
