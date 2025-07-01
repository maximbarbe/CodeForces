t = int(input())
for i in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        row = [*map(int, input().split())]
        grid.append(row)
    perm = [0] * (2*n)
    seen = {i+1: False for i in range(2*n)}
    for i in range(len(grid)):
        for j in range(len(grid)):
            seen[grid[i][j]] = True
            perm[(i + j + 1)] = grid[i][j]
    idx = perm.index(0)
    for key, val in seen.items():
        if seen[key] == False:
            perm[idx] = key
            break
    print(*perm)