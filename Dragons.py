s, n = map(int, input().split())
vals = []
for i in range(n):
    x, y = map(int, input().split())
    vals.append((x, y))
vals.sort(key=lambda el:(el[0], -el[1]))
for x, y in vals:
    if x >= s:
        print("NO")
        exit()
    else:
        s += y
else:
    print("YES")