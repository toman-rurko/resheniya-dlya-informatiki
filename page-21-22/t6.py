n = int(input())
step = 0
while n > 0:
    step += 1
    i = 0
    while 2 ** i <= n:
        i += 1
    i -= 1
    n -= 2 ** i
if step % 2 == 0:
    print('SECOND WINS')
else:
    print('FIRST WINS')
