from collections import Counter
from math import ceil
n = int(input())
vals = [*map(int, input().split())]

c = Counter(vals)
if max(c.values()) <= ceil(n/2):
    print("YES")
else:
    print("NO")