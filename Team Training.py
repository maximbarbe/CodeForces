t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    vals = [*map(int, input().split())]
    
    vals.sort(reverse=True)
    current_min = None
    cur = 0
    res = 0
    for i in range(len(vals)):
        current_min = vals[i]
        cur += 1
        
        if current_min * cur >= x:
            res += 1
            cur = 0
    print(res)