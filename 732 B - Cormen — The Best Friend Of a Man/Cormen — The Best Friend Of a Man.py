n, k = map(int, input().split())
vals = [*map(int, input().split())]
res = 0
if n == 1:
    print(0)
    print(vals[0])
    exit()
for i in range(1, len(vals) - 1):
    if vals[i - 1] + vals[i] < k and vals[i] + vals[i + 1] < k:
        needed = min(k - vals[i - 1] - vals[i], k - vals[i] - vals[i + 1])
        res += needed
        vals[i] += needed
for i in range(len(vals) - 1):
    if vals[i] + vals[i + 1] < k:
        needed = k - vals[i + 1] - vals[i]
        res += needed
        vals[i] += needed
print(res)
print(*vals)