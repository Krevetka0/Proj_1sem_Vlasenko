# Описать функцию RectPS(x1,y1,х2,y2,P,S), вычисляющую периметр P и площадь S
# прямоугольника со сторонами, параллельными осям координат, по координатам (х1, y1),
# (х2, y2) его противоположных вершин (x1, y1, x2, y2 — входные, P и S — выходные
# параметры вещественного типа). С помощью этой функции найти периметры и площади
# трех прямоугольников с данными противоположными вершинами.
def rectps(x1, y1, x2, y2):
    a = abs(x1) + abs(x2)
    b = abs(y1) + abs(y2)
    p = (a + b) * 2
    s = a * b
    return p, s


print(rectps(float(input('x1= ')), float(input('y1= ')), float(input('x2= ')), float(input('y2= '))))
print(rectps(float(input('x1= ')), float(input('y1= ')), float(input('x2= ')), float(input('y2= '))))
print(rectps(float(input('x1= ')), float(input('y1= ')), float(input('x2= ')), float(input('y2= '))))
