from functools import lru_cache
import sys


sys.setrecursionlimit(10**4)


MOD = 998_244_353
@lru_cache(None)
def fact(n):
    if n == 0:
        return 1
    else:
        return (n*fact(n-1)%MOD)%MOD
    
t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 1:
        print(0)
    else:
        print((fact(n//2)*fact(n//2))%MOD)