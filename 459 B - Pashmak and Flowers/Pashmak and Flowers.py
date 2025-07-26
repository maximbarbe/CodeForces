from collections import Counter
from math import comb
n = int(input())
vals = [*map(int, input().split())]
c = Counter(vals)
diff = max(vals) - min(vals)
res = 0
for v in sorted(set(vals), reverse=True):
    if diff == 0:
        res += (c[v] * (c[v] - 1))//2
    else:
        res += c[v] * c[v-diff]
print(diff, res)