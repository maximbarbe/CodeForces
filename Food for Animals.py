t = int(input())
for i in range(t):
    a,b,c,x,y = map(int, input().split())
    x = max(0, x -a)
    y = max(0, y - b)
    if x + y <= c:
        print("YES")
    else:
        print("NO")