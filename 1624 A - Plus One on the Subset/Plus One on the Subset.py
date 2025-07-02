t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    print(max(vals) - min(vals))