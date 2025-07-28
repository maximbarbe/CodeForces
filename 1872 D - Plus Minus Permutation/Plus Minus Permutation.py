from math import lcm

t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    
    res = 0
    n_x = n//x
    n_y = n//y
    combined = n//lcm(x, y)
    n_x -= combined
    n_y -= combined
    
    res = (n*(n+1))//2 - ((n-n_x)*(n-n_x + 1))//2
    res -= (n_y*(n_y + 1))//2
    
    print(res)