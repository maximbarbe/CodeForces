n = int(input())
dims = []
heights = []
for i in range(n):
    wi, hi = map(int, input().split())
    dims.append((wi, hi))
    heights.append(hi)
heights.sort()
s = 0
res = []
for w, h in dims:
    s += w
for wi, hi in dims:
    if hi == heights[-1]:
        res.append((s - wi)*heights[-2])
    else:
        res.append((s - wi)*heights[-1])
print(*res)
