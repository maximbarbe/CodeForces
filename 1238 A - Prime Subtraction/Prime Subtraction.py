t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(("YES","NO")[x==y+1])