n, k = map(int, input().split())
maximum = 0
cur = 0
for i in range(n):
    a, b = map(int, input().split())
    cur += b - a + 1
if cur % k == 0:
    print(0)
else:
    print(k - (cur % k))