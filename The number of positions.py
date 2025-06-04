n, a, b = map(int, input().split())
res = 0
for i in range(n):
    if i <= b and n - i - 1 >= a:
        res += 1
print(res)