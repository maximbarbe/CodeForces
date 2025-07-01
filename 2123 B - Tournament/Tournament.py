t = int(input())
for i in range(t):
    n, j, k = map(int, input().split())
    vals = [*map(int, input().split())]
    strength = vals[j - 1]
    if k == 1:
        if strength != max(vals):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")