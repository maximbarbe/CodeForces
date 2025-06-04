n = int(input())
collided = {i:False for i in range(1, n+1)}
grid = []
for i in range(n):
    grid.append([*map(int, input().split())])
for i in range(n):
    for j in range(n):
        match grid[i][j]:
            case 1:
                collided[i+1] = True
            case 2:
                collided[j+1] = True
            case 3:
                collided[i+1] = True
                collided[j+1] = True
            case _:
                continue
res = [k for k in collided.keys() if not collided[k]]
print(len(res))
if res:
    print(*res)