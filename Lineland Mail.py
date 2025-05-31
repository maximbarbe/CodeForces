n = int(input())
points = [*map(int, input().split())]
for i in range(n):
    mini, maxi = None, None
    if i == 0:
        mini = points[i + 1] - points[i]
        maxi = points[-1] - points[i]
    elif i == n-1:
        mini = points[i] - points[i - 1]
        maxi = points[i] - points[0]
    else:
        mini = min(points[i + 1] - points[i], points[i] - points[i - 1])
        maxi = max(points[i] - points[0], points[-1] - points[i])
    print(mini, maxi)