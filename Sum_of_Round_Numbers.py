from math import log10, floor

t = int(input())
for i in range(t):
    n = int(input())
    max_pow = floor(log10(n)) 
    factors = []
    while n != 0:
        if n // (10 ** (max_pow)) != 0:
            factors.append(n // (10 ** (max_pow)) * (10 ** (max_pow)))
            n -= n // (10 ** (max_pow)) * (10 ** (max_pow))
        max_pow -= 1
    print(len(factors))
    print(*factors)