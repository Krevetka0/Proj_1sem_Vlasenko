# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.
f1 = open('text18-4.txt', 'r', encoding='UTF-8')
a = f1.read()
f1.close()

f1 = open('text18-4.txt', 'w', encoding='UTF-8')
f1.writelines(a)
f1.close()

f1 = open('text18-4.txt', 'a', encoding='UTF-8')
c = len([i for i in a if i.isalpha()])
f1.write('\n')
f1.write('Количество букв: ')
f1.writelines(str(c))
f1.close()

f2 = open('new_text18-4.txt', 'w', encoding='UTF-8')
b = a.lower()
f2.writelines(b)
f2.close()
