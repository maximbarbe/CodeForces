n, m, a, b = map(int, input().split())
if b/ m < a:
    price = (n // m) * b
    n %= m
    if b < a * n:
        price += b
    else:
        price += a * n
    print(price)
else:
    print(n * a)