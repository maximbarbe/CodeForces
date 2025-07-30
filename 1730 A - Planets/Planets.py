from collections import Counter

t = int(input())
for i in range(t):
    n, cost = map(int, input().split())
    res = 0
    c = Counter([*map(int, input().split())])
    for k in c.keys():
        res += min(c[k], cost)
    print(res)