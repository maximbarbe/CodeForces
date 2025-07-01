from math import floor, sqrt

def is_composite(n):
    if n % 2 == 0:
        return True
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if n % i == 0:
            return True
    return False

n = int(input())
i = 4
while i < n:
    if is_composite(i) and is_composite( n- i):
        print(i, n - i)
        break
    else:
        i += 1