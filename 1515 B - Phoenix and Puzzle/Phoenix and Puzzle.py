from math import sqrt

for i in range(int(input())):
    n = int(input())
    if n == 2 * int(sqrt(n//2))**2 or n == 4 *int(sqrt(n//4))**2:
        print("YES")
    else:
        print("NO")