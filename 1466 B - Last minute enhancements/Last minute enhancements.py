from collections import Counter
for i in range(int(input())):
    n = int(input())
    vals = [*map(int, input().split())]
    res = 0
    c = Counter(vals)
    for key, value in c.items():
        res += 1
        if value > 1:
            if c[key + 1] == 0:
                res += 1
            else:
                c[key + 1] += 1
    print(res)