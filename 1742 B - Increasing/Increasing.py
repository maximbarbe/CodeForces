t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    print("YES" if len(vals) == len(set(vals)) else "NO")