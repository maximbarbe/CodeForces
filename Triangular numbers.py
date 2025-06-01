from math import sqrt
n = int(input())
delta = sqrt(1 + 8*n)
if int(delta) == delta and (1 + int(delta))%2 == 0:
    print("YES")
else:
    print("NO")