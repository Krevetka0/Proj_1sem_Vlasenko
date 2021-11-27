# Дан список размера N. Найти значение его последнего локального максимума (локальный
# максимум — это элемент, который больше любого из своих соседей).
import random
spisok = []
a = []
N = int(input('Введите размер списка: '))
for i in range(N):
    spisok.append(random.randint(0, 100))
print('Вот какой список мы получили: ', spisok)
spisok = [-1] + spisok + [-1]
for i in range(1, len(spisok) - 1):
    if spisok[i] > spisok[i + 1]:
        if spisok[i] > spisok[i - 1]:
            a.append(spisok[i])
print('Локальные максимумы в списке: ', *a)
print('Значение последнего локального максимума:', a[-1])
