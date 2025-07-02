n, a, b, c = map(int, input().split())
dp = [0]*(n + 1)
dp[0] = 1
for i in range(1, n + 1):
    if a <= i:
        if dp[i - a] != 0:
            dp[i] = max(dp[i], 1 + dp[i - a])
    if b <= i:
        if dp[i - b] != 0:
            dp[i] = max(dp[i], 1 + dp[i - b])
    if c <= i:
        if dp[i - c] != 0:
            dp[i] = max(dp[i], 1 + dp[i - c])
print(dp[n] - 1)