from collections import defaultdict
from math import inf
import heapq

def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

for i in range(int(input())):
    n,k,a,b = map(int, input().split())
    pos = []
    for j in range(n):
        x, y = map(int, input().split())
        pos.append((x, y))
    if a <= k and b <= k:
        print(0)
        continue
    elif a <= k or b <= k:
        if a <= k:
            b, a = a, b
        dist_a = min([dist(pos[a - 1], pos[i])  for i in range(k)])
        print(dist_a)
                
        
    else:
        d1 = dist(pos[a -1], pos[b-1])
        if k == 0:
            print(d1)
            continue
        dist_a = min([dist(pos[a - 1], pos[i])  for i in range(k)])
        dist_b = min([dist(pos[b - 1], pos[i]) for i in range(k)] )
        print(min(dist_a + dist_b, d1))