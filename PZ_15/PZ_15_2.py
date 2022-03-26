#  Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
import random
x, y = [int(input(i)) for i in ('Кол-во строк:', 'Кол-во столбцов:')]
matrix = [[random.randint(-2, 2) for i in range(x)] for j in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)
