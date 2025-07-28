from collections import defaultdict
from bisect import bisect_right

n = int(input())
vals = [*map(int, input().split())]

seen = defaultdict(lambda:[])
prefix = [0]*n
suffix = [0]*n
for i in range(n):
    if i == 0:
        prefix[i] = vals[i]
        suffix[n - 1 - i] = vals[n - 1 - i]
    else:
        prefix[i] = prefix[i - 1] + vals[i]
        suffix[n - 1 - i] = suffix[n - i] + vals[n - 1 - i]
s = prefix[-1]
for i in range(n):
    seen[prefix[i]].append(i)
    
res = 0
cur = 0
for i in range(n-1,-1,-1):
    cur = suffix[i]
    if cur * 3 == s:
        res += bisect_right(seen[cur], i-2)
print(res)