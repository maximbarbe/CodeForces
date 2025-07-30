t = int(input())
for i in range(t):
    n = int(input())
    s = [*map(int, input().split())]
    f = [*map(int, input().split())]
    i1 = i2 = 0
    res = []
    prev_ended = -1
    while i1 != n and i2 != n:
        if s[i1] > prev_ended:
            res.append(f[i2] - s[i1])
            prev_ended = f[i2]
            i1 += 1
            i2 += 1
        else:
            res.append(f[i2] - prev_ended)
            prev_ended = f[i2]
            i1 += 1
            i2 += 1
        
    print(*res)