n, m = map(int, input().split())
matches = []
res = 0
for i in range(m):
    a, b = map(int, input().split())
    matches.append((a, b))
matches.sort(key=lambda b: -b[1])
for i in range(m):
    if n == 0:
        break
    a, b = matches[i]
    if a > n:
        res += n*b
        break
    else:
        n -= a
        res += a*b
print(res)

