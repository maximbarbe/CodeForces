from math import lcm
t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    if lcm(l, l+1) > r:
        print(-1, -1)
    else:
        print(l, l + 1)