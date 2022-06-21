# 6 Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее арифметическое.
from random import randint
x, y = int(input('Столбцы: ')),  int(input('Строки: '))
matrix = [[randint(-10, 10) for i in range(x)] for j in range(y)]
print('Исходная матица: ')
for i in matrix:
    print(i)
h = []
for i in matrix:
    for o in i:
        if o > 0 and o % 2 == 0:
            h.append(o)
print("Положительные четные элементы: ", h, '\nСумма: ' + str(sum(h)),
      '\nСреднее арифметическое: ' + str(sum(h) / len(h)))
