from math import log
from functools import lru_cache


@lru_cache(None)
def r(n, k):
    if k == 1:
        return n
    res = 0
    while True:
        if k > n:
            res += n
            break
        else:
            p = int(log(n, k))
            res += 1
            n -= pow(k, p)
    return res

t = int(input())
for i in range(t):
    n, k = map(int, input().split())

    print(r(n, k))