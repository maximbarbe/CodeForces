from math import ceil

t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if c/b == a:
        print(1, -1)
    elif c / b < a:
        if c <= a:
            print(-1, b)
        else:
            print(1, b)
        
    else:
        print(1, -1)