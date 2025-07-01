from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    c = Counter(vals)
    keys = set()
    for k in c.keys():
        if c[k] > 1:
            keys.add(k)
    cur = 0
    res = 0
    while len(keys) != 0:
        res += 1
        
        if c[vals[cur]] > 1:
            c[vals[cur]] -= 1
            if c[vals[cur]] == 1:
                keys.remove(vals[cur])
        cur += 1
    print(res)