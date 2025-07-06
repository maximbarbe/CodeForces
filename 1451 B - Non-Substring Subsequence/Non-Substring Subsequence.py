from functools import lru_cache


t = int(input())
for i in range(t):
    n,q = map(int, input().split())
    s = input()
    for j in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if s[l] in s[:l] or s[r] in s[r+1:]:
            print("YES")
        else:
            print('NO')