from math import dist
n, k = map(int, input().split())
points = []
res = 0
for i in range(n):
    x, y=  map(int, input().split())
    points.append((x, y))
for i in range(1, n):
    res += dist(points[i], points[i - 1])
res = (res*k)/50
print(res)