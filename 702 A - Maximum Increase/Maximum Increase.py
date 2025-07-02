n = int(input())
cur = prev = 0
res = 0
vals = [*map(int, input().split())]
for v in vals:
    if v > prev:
        cur += 1
        prev = v
    else:
        cur = 1
        prev = v
    res = max(res, cur)
print(res)