n = int(input())
vals = [*map(int, input().split())]
pref_sum = [0]*(n + 1)
pref_sum_sorted = [0]*(n+1)
for i in range(n):
    pref_sum[i + 1] = vals[i] + pref_sum[i]
vals.sort()
for i in range(n):
    pref_sum_sorted[i + 1] = vals[i] + pref_sum_sorted[i]

q = int(input())
for i in range(q):
    type,l,r = map(int, input().split())
    if type == 1:
        print(pref_sum[r] - pref_sum[l - 1])
    else:
        print(pref_sum_sorted[r] - pref_sum_sorted[l - 1])