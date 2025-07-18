from collections import Counter, defaultdict

n = int(input())
vals = [*map(int, input().split())]
m = max(vals)
c = Counter(vals)
dp = [[0 for i in range(m + 3)] for j in range(2)]
for i in range(m, -1, -1):
    if c[i] == 0:
        dp[0][i] = max(dp[0][i + 1], dp[1][i + 1])
        dp[1][i] = max(dp[0][i + 1], dp[1][i + 1])
    else:
        dp[0][i] = c[i] * i + max(dp[0][i + 2], dp[1][i + 2])
        dp[1][i] = max(dp[0][i + 1], dp[1][i + 1])
print(max(dp[0][0], dp[1][0]))