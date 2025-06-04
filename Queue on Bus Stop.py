n, m = map(int, input().split())
res = 0
cur = 0
vals = [*map(int, input().split())]
for v in vals:
    if cur + v > m:
        res += 1
        cur = v
    else:
        cur += v
if cur:
    res += 1
print(res)