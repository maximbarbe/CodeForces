t = int(input())
for i in range(t):
    n = int(input())
    if n == 2:
        print(-1)
        continue
    res = [[i*n + j + 1 for j in range(n)] for i in range(n)]
    for j in range(n):
        col = []
        for i in range(n):
            col.append(res[i][j])
        if j % 2 == 0:
            col = [col[-1]] + col[:-1]
        else:
            col = col[1:] + [col[0]]
        for i in range(n):
            res[i][j] = col[i]
    for row in res:
        print(*row)