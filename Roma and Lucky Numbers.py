n, k = map(int, input().split())
res = 0
vals = [*map(int, input().split())]
for v in vals:
    v = str(v)
    c = 0
    for char in v:
        if char in "47":
            c += 1
    if c <= k:
        res += 1
print(res)