# Составить генератор (yield), который выводит из строки только буквы.
def letters(n):
    yield from [i for i in n if i.isalpha()]


print('Буквы в строке:', ''. join([c for c in letters(input("Введите строку:"))]))
