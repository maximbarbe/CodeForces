from functools import lru_cache
import sys


t = int(input())
for i in range(t):
    n = int(input())
    arr = [*map(int, input().split())]
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for a in range(n -1, -1, -1):
        for b in range(1, n+1):
            if a == b:
                dp[a][b] = 1
            elif b < a:
                continue
            elif arr[a] != arr[b - 1]:
                dp[a][b] = max(dp[a + 1][b], dp[a][b - 1])
            else:
                dp[a][b] = 2 + dp[a + 1][b - 1]
    if dp[0][-1] - 1 >= 3:
        print("YES")
    else:
        print("NO")