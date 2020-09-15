def F(x):
    return x * x + 16 * x + 15

a, b = map(int, input().split())
m = 0
for t in range(a, b+1):
    if F(t) > 0:
        m += 1
print(m)
