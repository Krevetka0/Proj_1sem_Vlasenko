# 45 В матрице найти максимальный положительный элемент, кратный 4.
from random import randint
n = int(input("Столбцы: "))
m = int(input("Строки: "))

matrix = [[randint(-2, 12) for j in range(n)] for i in range(m)]
print('Исходная матрица')
for i in matrix:
    print(i)
four = []
for i in matrix:
    for element in i:
        if element > 0 and element % 4 == 0:
            four.append(element)

print("Максимальный положительный элемент, кратный 4:", max(four))
