t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    minimum = 99
    for c in range(a,b+1):
        minimum = min(minimum, (c-a)+(b-c))
    print(minimum)