#вводим строку текста
string = input()

#находим половину от длины строки
half = len(string) // 2

#первая часть строки
first = string[:half]

#вторая часть строки
second = string[len(string)-half::][::-1]

#проверяем
isPalindrom = (first == second)

#выводим ответ
print('YES' if isPalindrom else 'NO')
