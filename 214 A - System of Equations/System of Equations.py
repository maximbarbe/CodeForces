from math import floor, sqrt

res = 0
n, m = map(int, input().split())
for a in range(n+1):
    for b in range(m+1):
        if a**2 + b == n and a + b**2 == m:
            res += 1
print(res)