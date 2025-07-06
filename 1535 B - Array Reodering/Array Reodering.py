from math import gcd

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    evens = []
    odds = []
    for v in vals:
        if v % 2 == 0:
            evens.append(v)
        else:
            odds.append(v)
    res = len(evens)*len(odds) + (len(evens) * (len(evens) - 1))//2
    for i in range(len(odds) - 1):
        for j in range(i + 1, len(odds)):
            if gcd(odds[i], odds[j]) > 1:
                res += 1
    print(res)