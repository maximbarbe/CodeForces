from math import inf
 
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    vals = [*map(int, input().split())]
    closest = [None]*n + [n]
    for j in range(n-1, -1, -1):
        if vals[j] == 1:
            closest[j] = j
        else:
            closest[j] = closest[j + 1]
    dp = [0]*(n+2)
    for i in range(n-k, -1, -1):
        if closest[i] - i >= k:
            dp[i] = max(1 + dp[i + k + 1], dp[i + 1])
        else:
            dp[i] = dp[i + 1]
    print(dp[0])