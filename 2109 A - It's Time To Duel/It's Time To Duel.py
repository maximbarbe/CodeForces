t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    if all(vals) or any([vals[i] == vals[i + 1] == 0 for i in range(n-1)]):
        print("YES")
    else:
        print("NO")
        