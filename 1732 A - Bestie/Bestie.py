from math import gcd

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    g = gcd(*vals)
    if g == 1:
        print(0)
    else:
        res = 0
        for j in range(len(vals) - 1, -1, -1):
            if gcd(g, gcd(vals[j], j + 1)) == 1:
                res = n-j
                break
        print(min(res, 3))
