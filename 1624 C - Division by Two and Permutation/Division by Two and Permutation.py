from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    for j in range(len(vals)):
        while vals[j] > n:
            vals[j] = int(vals[j]/2)
    
    c = Counter(vals)
    for j in range(len(vals)):
        cur = vals[j]
        if c[cur] > 1:
            while True:
                c[cur] -= 1
                cur = int(cur/2)
                c[cur] += 1
                
                if c[cur] == 1:
                    break
            if cur == 0:
                print("NO")
                break
            vals[j] = cur
    else:
        vals.sort()
        for i in range(len(vals)):
            if vals[i] != i + 1:
                break
        else:
            print("YES")
            
        