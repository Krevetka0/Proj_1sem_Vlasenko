# 35 В матрице элементы кратные трём увеличить в 3 раза.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print('Исходная матрица')
for i in matrix:
    print(i)

for i in matrix:
    for j in i:
        if j % 3 == 0:
            j *= 3
        print(j, end=' ')
    print()
