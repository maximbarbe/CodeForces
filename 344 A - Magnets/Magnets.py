n = int(input())
cur = None
res = 0
for i in range(n):
    m = input()
    if m != cur:
        res += 1
        cur = m
print(res)