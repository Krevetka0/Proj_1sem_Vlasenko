# Дан список размера N. Переставить в обратном порядке элементы список,
# расположенные между его минимальным и максимальным элементами, включая
# минимальный и максимальный элементы.
import random

spisok = []
N = int(input('Введите размер списка: '))
for i in range(N):
    spisok.append(random.randint(0, 100))
print('Мы получили список: ', spisok)
Min = 0
Max = 0
for i in range(len(spisok)):
    if spisok[i] > spisok[Max]:
        Max = i
    elif spisok[i] < spisok[Min]:
        Min = i
b = spisok[Min:(Max + 1)] if Min < Max else spisok[Max:(Min + 1)]
print('Диапазон от миниамального до максимального:', b)
b.reverse()
print('Развернем наш диапазон', b)
