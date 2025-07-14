from math import floor, ceil
for i in range(int(input())):
    n = int(input())
    n1 = floor(n/3)
    n2 = ceil(n/3)
    minimum = min(n1, n2, key=lambda el:(abs(n-3*el), el))
    print(n-2*minimum, minimum)