from math import inf, floor, ceil, log2, gcd, prod
from itertools import combinations
import heapq
from collections import defaultdict, deque, Counter
import sys
 
MOD = 10**9 + 7
 
 
primes = [2, 3, 5, 7]
 
t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    n = r - l
    notgood = 0
    for j in range(1, 5):
        comb = combinations(primes, j)
        for c in comb:
            if j in [1, 3]:
                notgood += r//prod(c) - (l - 1)//prod(c)
            else:
                notgood -= r//prod(c) - (l - 1)//prod(c)
    print(n-notgood + 1)