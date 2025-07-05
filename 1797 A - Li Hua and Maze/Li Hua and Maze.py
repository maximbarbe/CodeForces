t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) in [(1, 1), (n, 1), (n, m), (1, m)] or (x2, y2) in [(1, 1), (n, 1), (n, m), (1, m)]:
        print(2)
    elif x1 == 1 or y1 == 1 or x1 == n or y1 == m or x2 == 1 or x2 == n or y2 == 1 or y2 == m:
        print(3)
    else:
        print(4)