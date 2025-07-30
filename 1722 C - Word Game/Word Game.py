from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    grid = []
    c = Counter()
    for j in range(3):
        
        words = input().split()
        for w in words:
            c[w] += 1
        grid.append(words)
    scores = [0, 0, 0]
    for j in range(3):
        for w in grid[j]:
            if c[w] == 1:
                scores[j] += 3
            elif c[w] == 2:
                scores[j] += 1
    print(*scores)