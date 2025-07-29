t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    vals = [*map(int, input().split())]
    s = sum(vals)
    if s % x != 0:
        print(len(vals))
    else:
        els = []
        for i, v in enumerate(vals):
            if v % x != 0:
                els.append(i)
        if not els:
            print(-1)
        else:
            first = els[0]
            last = els[-1]
            print(max(n - (first + 1), last))