t = int(input())
for i in range(t):
    
    n, m = map(int, input().split())
    for i in range(n):
        row = []
        for j in range(m):
            if (i%4, j%4) in [(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 3)]:
                row.append(1)
            else:
                row.append(0)
            
        print(*row)