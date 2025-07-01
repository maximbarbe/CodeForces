n, m = map(int, input().split())
vals = [*map(int, input().split())]
vals.sort()
min_diff = 10**9
for i in range(len(vals) -n + 1):
    if vals[i + n - 1] - vals[i] < min_diff:
        min_diff = vals[i + n - 1] - vals[i]
print(min_diff)