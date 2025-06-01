n, m = map(int, input().split())
buttons = [*map(int, input().split())]
res = []
for i in range(1, n+1):
    for bi in buttons:
        if i >= bi:
            res.append(bi)
            break
print(*res)