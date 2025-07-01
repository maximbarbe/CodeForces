n,m = map(int, input().split())
vals = [1] + [*map(int, input().split())]
res = 0
for i in range(1, len(vals)):
    if vals[i] < vals[i - 1]:
        res += n + vals[i] - vals[i - 1]
    else:
        res += vals[i] - vals[i - 1]
print(res)