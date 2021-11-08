# Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B < 3».
while True:    # обработка исключений
    try:
        A = int(input('Введите целое число A: '))
        break
    except ValueError:
        print('Нужно целое число!')

while True:    # обработка исключений
    try:
        B = int(input('Введите целое число B: '))
        break
    except ValueError:
        print('Нужно целое число!')

if A > 2 and B < 3:
    print('Неравенства A > 2 и B < 3 верны!')
else:
    print('Неравенства A > 2 и B < 3 не верны!')
