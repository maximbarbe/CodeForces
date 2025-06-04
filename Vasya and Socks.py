n, m = map(int, input().split())
res = 0

while n != 0:
    res += 1
    n -= 1
    if res % m == 0:
        n += 1
print(res) 