from math import floor, ceil

n = int(input())
f = False
for i in range(n):
    num = int(input())
    if num%2 == 0:
        print(num//2)
    else:
        if not f:
            print(ceil(num/2))
        else:
            print(floor(num/2))
        f ^= True