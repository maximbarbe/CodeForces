from math import inf, floor, ceil, log2, gcd
import heapq
from collections import defaultdict, deque, Counter
import sys
 
MOD = 10**9 + 7
 
 
for i in range(int(input())):
    a, b, k = map(int, input().split())
    g = gcd(a, b)
    if a <= k and b <= k:
        print(1)
    else:
        dx = a//g
        dy = b//g
        if dx <= k and dy <= k:
            print(1)
        else:
            print(2)