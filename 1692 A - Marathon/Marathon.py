t = int(input())
for i in range(t):
    a, b, c, d= map(int, input().split())
    vals = sorted([a, b, c, d], reverse=True)
    print(vals.index(a))