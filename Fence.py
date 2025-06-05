n, k = map(int, input().split())
h = [*map(int, input().split())]
pref = [0]*(n+1)
for i in range(1, n+1):
    pref[i] = pref[i - 1] + h[i - 1]
minimum = 10**9
idx = None
for i in range(1, n+1):
    if i + k - 2 >= n:
        break
    cur = pref[i + k - 1] - pref[i - 1]
    if cur < minimum:
        minimum = cur
        idx  = i
print(idx)