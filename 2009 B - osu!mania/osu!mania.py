t = int(input())
for i in range(t):
    n = int(input())
    res = []
    for j in range(n):
        res.append(input().index("#") + 1)
    print(*res[::-1])