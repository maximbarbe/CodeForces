n = int(input())
res = []
if n in [1, 2]:
    print(1)
    print(1)
    exit()
if n == 3:
    print(2)
    print(1, 3)
    exit()
if n == 4:
    print(4)
    print(3, 1, 4, 2)
    exit()
if n%2 == 0:
    for i in range(n//2):
        res.append(i + 1)
        res.append(n//2 + i + 1)
else:
    for i in range(n//2):
        res.append(i + 1)
        res.append(n//2 + i + 2)
    res.append(n//2 + 1)
print(len(res))
print(*res)