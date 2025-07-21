from math import inf

n, v = map(int, input().split())
dp = [[inf for i in range(n)] for j in range(v+1)]
for i in range(v+1):
    dp[i][-1] = 0
for j in range(n-2, -1, -1):
    for i in range(v+1):
        if i == 0:
            for k in range(1, v+1):
                dp[i][j] = min(k*(j + 1) + dp[k - 1][j + 1], dp[i][j])
        else:
            for k in range(i, v+1):
                dp[i][j] = min((k - i)*(j + 1) + dp[k - 1][j + 1], dp[i][j])
print(dp[0][0])