# 24 В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица: ")
for i in matrix:
    print(i)

h = []
for i in matrix:
    for o in i:
        if o < 0:
            h.append(o)

print("Новый массив: ", h)
print("Размер массива: ", len(h))
