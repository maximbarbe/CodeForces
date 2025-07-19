t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    prev = 0
    res = 0
    for v in vals:
        if v < prev:
            res += 1
            prev = 0
        else:
            prev = v
    print(res)