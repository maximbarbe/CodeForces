from math import ceil, floor
n,m = map(int, input().split())
res = 0
temp = m
to_add = set()
while temp % 5 != 0:
    to_add.add(temp%5)
    temp -= 1
for i in range(1, n + 1):
    res += floor(m/5)
    if 5 - i%5 in to_add:
        res += 1
print(res)