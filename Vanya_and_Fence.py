n, h = map(int, input().split())
res = 0
vals = [*map(int, input().split())]
for val in vals:
    if val > h:
        res += 2
    else:
        res += 1
print(res)