from math import gcd


t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    minimum = 10**6
    for i in range(len(vals) - 1):
        for j in range(i + 1, len(vals)):
            minimum = min(minimum, gcd(vals[i], vals[j]))
    if minimum <= 2:
        print("YES")
    else:
        print('NO')