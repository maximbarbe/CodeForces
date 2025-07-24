from functools import lru_cache
import sys

MOD = 10**9 + 7

    
t = int(input())
ns = [*map(int, input().split())]
ks = [*map(int, input().split())]
for k in ks:
    print(pow(2, k, MOD))