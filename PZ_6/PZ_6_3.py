# Дан список размера N. Переставить в обратном порядке элементы список,
# расположенные между его минимальным и максимальным элементами, включая
# минимальный и максимальный элементы.
from random import randint

spisok = []
N = int(input('Введите размер списка: '))
for i in range(0, N):
    spisok.append(randint(0, 100))
print('Мы получили такой список:', spisok)

Max = 0
Min = 0
for i in range(len(spisok)):
    if spisok[Max] < spisok[i]:
        Max = i
    elif spisok[Min] > spisok[i]:
        Min = i

b = spisok[Max:(Min + 1)] if Min > Max else spisok[Min:(Max + 1)]
print('Диапазон от минимального до максимального:', b)
b.reverse()
print('Развернем наш диапазон:', b)

if Min < Max:
    for i in range(len(b)):
        del spisok[Min + i]
        spisok.insert(Min + i, b[i])
else:
    for i in range(len(b)):
        del spisok[Max + i]
        spisok.insert(Max + i, b[i])
print('Итоговый список: ', spisok)
