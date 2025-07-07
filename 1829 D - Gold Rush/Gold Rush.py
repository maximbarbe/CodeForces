from functools import lru_cache

@lru_cache(None)
def res(n, m):
    if n == m:
        return True
    elif n < m or n % 3 != 0:
        return False
    else:
        return res(n//3, m) or res(2*(n//3), m)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if res(n,m):
        print("YES")
    else:
        print("NO")