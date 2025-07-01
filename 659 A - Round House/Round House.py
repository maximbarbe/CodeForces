n, a, b = map(int, input().split())
b -= n*(b//n)
while b != 0:
    if b < 0:
        a -= 1
    elif b > 0:
        a += 1
    b -= 1
    if a == n+1:
        a = 1
    elif a == 0:
        a = n
print(a)