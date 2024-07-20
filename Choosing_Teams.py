n, k = map(int, input().split())
vals = sorted([*map(int, input().split())])
res = 0
for i in range(0, n-2, 3):
    if vals[i+2] +k <= 5:
        res += 1
print(res)