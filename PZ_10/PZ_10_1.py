# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:Исходные данные: Количество элементов: Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент
a = '-10 95 3 28 -45 -1 56 72'
f1 = open('new_file_1.txt', 'w')
f1.writelines(a)
f1.close()

f2 = open('new_file_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.writelines(a)
f2.write('\n')
f2.close()

f1 = open('new_file_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
c = str(len(k))
d = str(min(k))
f1.close()

f2 = open('new_file_2.txt', 'a', encoding='UTF-8')
f2.write('Количество элементов: ')
f2.writelines(c)
f2.write('\n')
f2.write('Минимальный элемент: ')
f2.writelines(d)
f2.write('\n')
f2.close()

f1 = open('new_file_1.txt')
a = [-10, 95, 3, 28, -45, -1, 56, 72]
maxi = a[0]
for i in a:
    if i > maxi:
        maxi = i

for i in range(len(a)):
    a[i] *= maxi
f1.close()

f2 = open('new_file_2.txt', 'a', encoding='UTF-8')
f2.write('Элементы, умноженные на первый максимальный элемент: ')
f2.writelines(str(a))
f2.close()
