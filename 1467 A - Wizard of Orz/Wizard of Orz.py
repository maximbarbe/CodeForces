t = int(input())
for i in range(t):
    n = int(input())
    res = []
    for j in range(min(n, 2)):
        res.append(9-j)
    for j in range(2, n):
        res.append((res[-1] + 1)%10)
    print("".join(map(str, res)))