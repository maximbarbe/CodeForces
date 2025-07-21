t = int(input())
for i in range(t):
    n = int(input())
    res = [0]*n
    vals = [*map(int, input().split())]
    cur = 0
    for i in range(len(vals) - 1, -1, -1):
        if vals[i] != 0:
            cur = max(cur, vals[i])
        
        if cur != 0:
            res[i] = 1
            cur -= 1
    print(*res)