# 21 В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
from random import randint
x, y = int(input('Столбцы: ')), int(input('Строки: '))
r = int(input('Номер строки: '))
matrix = [[randint(-5, 5) for j in range(x)] for i in range(y)]
print("Исходная матрица:")
for i in matrix:
    print(i)
sum1 = 0
prod = 1
for i in matrix[r - 1]:
    sum1 += i
    prod *= i
print('Сумма элементов:', sum1, '\nПроизведение элементов:', prod)
