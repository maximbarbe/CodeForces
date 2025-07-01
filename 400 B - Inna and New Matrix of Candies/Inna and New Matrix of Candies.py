n, m = map(int, input().split())
m = 0
distances = set()
for i in range(n):
    row = input()
    s = row.index("S")
    g = row.index("G")
    if g > s:
        print(-1)
        exit()
    distances.add(s - g)
print(len(distances))