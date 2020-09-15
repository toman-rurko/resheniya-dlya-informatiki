#подключаем функцию квадратного корня
from math import sqrt

#координаты для двух точек первого отрезка
x11, y11, x12, y12 = map(float, input().split())
#координаты для двух точек второго отрезка
x21, y21, x22, y22 = map(float, input().split())

#находим длину первого отрезка по уравнению прямой
len1 = sqrt( (x11-x12) ** 2 + (y11-y12) ** 2 )

#находим длину второго отрезка по уравнению прямой
len2 = sqrt( (x21 - x22) ** 2 + (y21-y22) ** 2 )

#выводим FIRST, усли первый короче, SECOND -- если второй,
#иначе EQUALS
if len1 == len2:
    print('EQUALS')
elif len1 < len2:
    print('FIRST')
else:
    print('SECOND')
print()

#дополнительно выведем дины каждого отрезка
print('first: {}'.format(len1))
print('second: {}'.format(len2))
