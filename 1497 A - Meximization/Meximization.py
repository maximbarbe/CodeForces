from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    c = Counter(vals)
    res = []
    for key in sorted(c.keys()):
        res.append(key)
        c[key] -= 1
    for key in c.keys():
        if c[key] > 0:
            res.extend([key]*c[key])
    print(*res)