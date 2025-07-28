from collections import Counter

n, k = map(int, input().split())

vals = [*map(int, input().split())]
c = Counter(vals)
count = 0
if k == 0 and min(vals) > 1:
    print(1)
    exit()
for v in sorted(set(vals)):
    if count + c[v] <= k:
        count += c[v]
    else:
        print(-1)
        exit()
    if count == k:
        print(v)
        exit()
