t = int(input())
for i in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    
    if a == b:
        print(0)
    elif abs(a-b) >= x:
        print(1)
    else:
        if x > r - l or (abs(r-b) < x and abs(l - b) < x) or (abs(r - a) < x and abs(l - a) < x):
            print(-1)
        elif (abs(r-b) >= x and abs(r -a )>= x) or (abs(l - a) >= x and abs(l - b) >= x):
            print(2)
        else:
            print(3)