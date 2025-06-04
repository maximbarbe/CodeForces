n,m,k = map(int, input().split())
vals = [*map(int, input().split())]
res = 0
for v in vals:
    if v == 1:
        if m >= 1:
            m -= 1
        else:
            res += 1
    else:
        if k >= 1:
            k -= 1
        elif m >= 1:
            m -= 1
        else:
            res += 1
print(res)
            