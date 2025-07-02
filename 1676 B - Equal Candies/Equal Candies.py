t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    m = min(vals)
    res = 0
    for v in vals:
        res += v - m
    print(res)