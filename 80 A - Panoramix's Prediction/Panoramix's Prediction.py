from math import sqrt, floor

n, m = map(int, input().split())

def is_prime(v):
    if v % 2== 0:
        return False
    else:
        for i in range(3, floor(sqrt(v)) + 1):
            if v % i == 0:
                return False
        else:
            return True



cur = n + 1
while not is_prime(cur):
    cur += 1
if cur == m:
    print("YES")
else:
    print("NO")