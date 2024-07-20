a, b = map(int, input().split())
res = 0
while a <= b:
    res += 1
    a*=3
    b *= 2
print(res)