n = int(input())
vals = [*map(int, input().split())]
best = vals[0]
worst = vals[0]
res = 0
for i in range(1, len(vals)):
    if vals[i] > best:
        res += 1
        best = vals[i]
    elif vals[i] < worst:
        res += 1
        worst = vals[i]
print(res)