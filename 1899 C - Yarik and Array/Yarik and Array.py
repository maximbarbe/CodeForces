from math import inf

t = int(input())
for i in range(t):
    n = int(input())
    dp = [[0 for i in range(n)] for j in range(2)]
    vals = [*map(int, input().split())]
    m = -inf
    cur = 0
    prev = None
    for v in vals:
        if cur + v < 0:
            cur = 0
            prev = None
        else:
            if prev == None:
                cur = v
                prev = v
                m = max(m, cur)
            else:
                if v % 2 != prev % 2:
                    cur += v
                    prev = v
                    m = max(m, cur)
                else:
                    if v < 0:
                        cur = 0
                        prev = None
                    else:
                        cur = v
                        prev = v
                        m = max(m, cur)
            
    
    if m == -inf:
        print(max(vals))
    else:
        print(m)