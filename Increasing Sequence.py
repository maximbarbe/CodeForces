from math import ceil

n, d = map(int, input().split())
vals = [*map(int, input().split())]
res = 0
for i in range(1, len(vals)):
    if vals[i] <= vals[i - 1]:
        moves = ceil((vals[i - 1] + 1 - vals[i])/d)
        res += moves
        vals[i] += moves * d

print(res)