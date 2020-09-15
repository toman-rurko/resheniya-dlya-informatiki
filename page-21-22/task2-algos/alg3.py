x = int(input())
l, m = 0, 0
while x > 0:
    m += 1
    if x % 3 != 0:
        l += 1
    x //= 3
print(l)
print(m)
