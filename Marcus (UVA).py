t = int(input())

def dfs(i, j, m, n, cmd, idx):
    if grid[i][j] == "#":
        return True
    directions = [(-1, 0), (0, 1), (0, -1)]
    commands = ["forth", "right", "left"]
    for ((x, y), c) in zip(directions, commands):
        if 0 <= i + x < m and 0 <= y + j < n and grid[i + x][j + y] == "IEHOVA#"[idx]:
            cmd.append(c)
            res = dfs(i + x, y+j, m, n, cmd, idx + 1)
            if res:
                return True
            else:
                cmd.pop()
    return False


for i in range(t):
    m, n = map(int, input().split())
    grid = []
    cmd = []
    src = None
    for i in range(m):
        row = input()
        grid.append(row)
        if i == m-1:
            for j in range(len(row)):
                if row[j] == "@":
                    src = (i, j)
                    break
    dfs(src[0], src[1],m, n, cmd, 0)
    print(" ".join(cmd))