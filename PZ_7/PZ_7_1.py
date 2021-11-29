# Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных)
# букв латинского алфавита.
List = []
while True:
    try:
        N = int(input('Введите целое число от 1 до 26: '))
        if 1 < N < 26:
            break
        else:
            print('Введите число от 1 до 26!!!')
    except ValueError:
        print('Нужно целое число!')
alp = []
while N:
    alp.append(chr(64 + N))
    N -= 1

alp.reverse()
print(alp)
