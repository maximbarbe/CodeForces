from math import log2, ceil

t = int(input())
for i in range(t):
    n = int(input())
    
    p = 2
    for k in range(2, ceil(log2(n+1)) +1):
        p *= 2
        cur = n/(p-1)
        if int(cur) == cur:
            print(int(cur))
            break