t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    while n != 0:
        res += n
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            n //= 2
    print(res)