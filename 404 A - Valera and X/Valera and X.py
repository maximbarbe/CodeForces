n = int(input())
grid = []
for i in range(n):
    grid.append(input())
    
x_letter =None
other_letter = None
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            if x_letter:
                if grid[i][j] != x_letter:
                    print('NO')
                    exit()
            else:
                x_letter = grid[i][j]
        else:
            if other_letter:
                if grid[i][j] != other_letter:
                    print('NO')
                    exit()
            else:
                if grid[i][j] == x_letter:
                    print("NO")
                    exit()
                else:
                    other_letter = grid[i][j]
print("YES")
                