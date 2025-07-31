from math import gcd

t = int(input())
for i in range(t):
    x = int(input())
    maximum = 0
    v = 0
    for y in range(1, x):
        if (new := gcd(x, y) + y) > maximum:
            v = y
            maximum = new
    print(v)