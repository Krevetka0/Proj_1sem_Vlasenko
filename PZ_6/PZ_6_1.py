#  Дан первый член A и знаменатель D геометрической прогрессии. Сформировать и
# вывести список размера 10, содержащий 10 первых членов данной прогрессии: A, A* D, A* D^2, A* D^3,....
A = float(input('Введите первый член геометрической прогрессии: '))
D = float(input('Введите знаменатель геометрической прогрессии: '))
List = []
for i in range(10):
    List.append(A * (D ** i))
print(List)