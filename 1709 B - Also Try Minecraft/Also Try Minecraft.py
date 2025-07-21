n, m = map(int, input().split())
vals = [*map(int, input().split())]
prefix = [0]*(n + 1)
suffix = [0]*(n + 1)
for i in range(1, len(vals)):
    if vals[i] >= vals[i - 1]:
        prefix[i + 1] = prefix[i]
    else:
        prefix[i + 1] = prefix[i] + vals[i - 1] - vals[i]
for i in range(len(vals) - 2, -1, -1):
    if vals[i] >= vals[i + 1]:
        suffix[i] = suffix[i + 1]
    else:
        suffix[i] = suffix[i + 1] + vals[i +1] - vals[i]
for j in range(m):
    a, b = map(int, input().split())
    if a < b:
        print(prefix[b] - prefix[a])
    else:
        print(suffix[b - 1] - suffix[a - 1])