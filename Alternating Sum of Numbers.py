t = int(input())
for _ in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = 0
    for i in range(len(vals)):
        if i % 2 == 0:
            res += vals[i]
        else:
            res -= vals[i]
    print(res)