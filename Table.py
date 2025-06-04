n, m = map(int, input().split())
edge = False
for i in range(n):
    row = [*map(int, input().split())]
    for j in range(m):
        if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and row[j] == 1:
            edge = True
if edge:
    print(2)
else:
    print(4)