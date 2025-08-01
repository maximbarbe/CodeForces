from itertools import permutations
from math import lcm


t = int(input())

for i in range(t):
    n = int(input())
    res = [None]*n
    if n % 2 == 0:
        for i in range(n//2):
            res[2*i] = 2*(i + 1)
            res[2*i + 1] = 2*i + 1
    else:
        res[0] = 1
        for i in range(n//2):
            res[2*(i + 1)] = 2*(i + 1)
            res[2*i + 1] = 2*(i + 1) + 1
    print(*res)
