# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.
L = [1, 64, 15, 90, 27]
a = [n * L[-1] for n in L[0:-1]]
print(a)