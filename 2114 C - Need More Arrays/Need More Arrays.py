t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = [vals[0]]
    for i in range(1, len(vals)):
        if vals[i] > res[-1] + 1:
            res.append(vals[i])
    print(len(res))