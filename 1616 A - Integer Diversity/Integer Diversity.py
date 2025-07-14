from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    c = Counter(vals)
    res = 0
    for k, v in c.items():
        if v == 1:
            res += 1
        else:
            if c[-k] == 0:
                res += 2
            else:
                res += 1
    print(res)