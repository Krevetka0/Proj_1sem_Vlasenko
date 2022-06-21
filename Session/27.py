# 27 Для каждого столбца матрицы с четным номером найти сумму ее элементов.
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Изначальная матрица: ")
for i in matrix:
    print(i)

n = 2
summa = 0
for i in matrix[1::2]:
    for e in i:
        summa += e
    print(str(n)+' строка. Сумма:', summa)
    n += 2
    summa = 0
