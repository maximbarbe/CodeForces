from math import gcd
y, w = map(int, input().split())
chances = 7 - max(y, w)
if chances == 6:
    print("1/1")
else:
    temp = gcd(chances, 6)
    print(f"{chances // temp}/{6 //temp}")