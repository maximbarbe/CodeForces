t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    a = bin(a)[2:]
    b = bin(b)[2:]
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))
    res = []
    for b1, b2 in zip(a, b):
        if b1 == b2:
            res.append("0")
        else:
            res.append("1")
    print(int("".join(res), 2))