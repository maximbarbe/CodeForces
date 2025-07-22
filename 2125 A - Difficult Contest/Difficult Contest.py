from math import inf, floor, ceil, log2
import heapq
from collections import defaultdict, deque, Counter
import sys
 
MOD = 10**9 + 7
 
 
for i in range(int(input())):
    s = input()
    letters = Counter(s)
    res = ""
    for key in sorted(letters.keys(), reverse=True):
        res += key * letters[key]
    print(res)