from math import gcd

t = int(input())
for i in range(t):
    n = int(input())
    while gcd(n, sum([int(c) for c in str(n)])) == 1:
        n += 1
    print(n)