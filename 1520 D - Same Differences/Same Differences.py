t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = 0
    seen = dict()
    for i in range(len(vals)):
        res += seen.get(vals[i] - i, 0)
        seen[vals[i] - i] = seen.get(vals[i] - i, 0) + 1
    print(res)
    