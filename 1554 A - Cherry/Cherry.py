t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    m = 0
    for i in range(len(vals) - 1):
        m = max(m, vals[i]*vals[i + 1])
    print(m)