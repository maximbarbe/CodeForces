n, k = map(int, input().split())
vals = [*map(int, input().split())]
while k != 0:
    for i in range(len(vals) - 1):
        if i % 2 == 1 and vals[i - 1] <vals[i] - 1  and vals[i] - 1>vals[i + 1]:
            vals[i] -= 1
            k -= 1
        if k == 0:
            break
print(*vals)