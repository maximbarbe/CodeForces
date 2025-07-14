from math import ceil

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if k > ceil(n/2):
        print(-1)
        continue
        
    x = 0
    y = 0
    c = 0
    for i in range(n):
        for j in range(n):
            if (i, j) == (x, y) and c != k:
                print("R",end="")
                x += 2
                y += 2
                c += 1
            else:
                print(".",end="")
        print()
                