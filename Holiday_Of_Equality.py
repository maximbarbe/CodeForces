n = int(input())
vals = [*map(int, input().split())]
maximum = max(vals)
res = 0
for val in vals:
    res += maximum - val
print(res)