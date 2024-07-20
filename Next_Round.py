n, k = map(int, input().split())
res = 0
vals = [*map(int, input().split())]
threshold = vals[k - 1]
for i in range(len(vals)):
    if vals[i] >= threshold and vals[i] > 0:
        res += 1
print(res)