t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    if len(set(vals)) == 1:
        print(-1)
        continue
    c = []
    b = []
    m = max(vals)
    for v in vals:
        if v == m:
            c.append(v)
        else:
            b.append(v)
    print(len(b), len(c))
    print(*b)
    print(*c)