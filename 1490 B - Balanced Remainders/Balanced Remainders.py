t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    v = [0]*3
    for c in vals:
        v[c%3] += 1
    res = 0
    more = 0
    target = n//3
    m = min(v)
    idx = v.index(m)
    for i in range(4):
        if v[idx] < target:
            needed = target - v[idx]
            res += target - v[idx]
            v[idx] = target
            v[(idx - 1)%3] -= needed        
        idx = (idx + 1)%3
    print(res)