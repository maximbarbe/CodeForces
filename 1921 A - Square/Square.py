n = int(input())
for i in range(n):
    minx = miny = 1001
    maxx = maxy = -1001
    for j in range(4):
        x, y = map(int, input().split())
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
    print((maxy-miny)*(maxx-minx))