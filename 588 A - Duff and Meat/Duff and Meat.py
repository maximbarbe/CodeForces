n = int(input())
prev_price = 101
res = 0
for i in range(n):
    a, p = map(int, input().split())
    if p < prev_price:
        prev_price = p
    res += a*prev_price
print(res)