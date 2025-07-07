from functools import lru_cache





t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    while n != 1:
        if n % 6 == 0:
            n //= 6
            res += 1
        elif n % 3 == 0:
            n *= 2
            res += 1
        else:
            print(-1)
            break
    else:
        print(res)