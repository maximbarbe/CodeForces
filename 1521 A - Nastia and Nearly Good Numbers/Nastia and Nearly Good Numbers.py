t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if b == 1:
        print("NO")
    else:
        print("YES")
        print(a*b, a*b - a, 2*a*b - a)