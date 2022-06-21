# 32 В матрице найти сумму элементов второй половины матрицы
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица:")
for i in matrix:
    print(i)
summa = 0
for i in range(len(matrix) // 2, len(matrix)):
    for e in matrix[i]:
        summa += e
print("Сумма элементов второй половины: ", summa)
