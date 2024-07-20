n = int(input())
res = 0
cur = 0
vals = [*map(int, input().split())]
for k in vals:

    if k == -1:
        cur += 1
    else:
        cur -= k
    res = max(cur, res)
print(res)