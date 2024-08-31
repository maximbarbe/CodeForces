n = int(input())
table = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    table[0][i] = 1
    table[i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        table[i][j] = table[i - 1][j] + table[i][j-1]
print(table[-1][-1])