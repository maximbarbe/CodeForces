import heapq
from math import ceil


t = int(input())
for i in range(t):
    moves = []
    vals = [i for i in range(1, int(input()) + 1)]
    while len(vals) > 1:
        b = vals.pop()
        a = vals.pop()
        moves.append((a, b))
        vals.append(ceil((a + b)/2))
        
    print(vals.pop())
    for a, b in moves:
        print(a, b)