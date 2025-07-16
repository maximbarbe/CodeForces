t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    if len(set(vals)) == 1:
        print("NO")
    else:
        print("YES")
        m = max(vals)
        v = []
        for k in vals:
            if k == m:
                v.append(1)
            else:
                v.append(2)
        print(*v)