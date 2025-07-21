t = int(input())
for i in range(t):
    n = int(input())
    if n <= 4:
        print(-1)
        continue
    perm = []
    for j in range(1, n+1):
        if j % 2 == 1 and j != 5:
            perm.append(j)
    perm.append(5)
    perm.append(4)
    for j in range(1, n + 1):
        if j % 2 == 0 and j != 4:
            perm.append(j)
    print(*perm)    