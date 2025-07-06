from math import gcd

t = int(input())

for i in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n//2 - 1, n//2, 1)
    else:
        left = 3
        right = n - 4
        while True:

            if gcd(left, right) == 1:
                print(left, right, 1)
                break
            else:
                left += 1
                right -= 1