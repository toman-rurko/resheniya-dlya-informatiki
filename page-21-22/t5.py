#вводим числитель, знаменатель
up, down = map(int, input().split())

#функция для нахождения НОДа
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

#записываем НОД
mygcd = gcd(up, down)

#выводим ответ
print('{} {}'.format(up//mygcd, down//mygcd))
