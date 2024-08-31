t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if k in [*map(int, input().split())]:
        print("YES")
    else:
        print("NO")