from math import inf
t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    dp = [[0 for i in range(n + 1)] for j in range(2)]
    dp[0][-2] = vals[-1]
    dp[1][-2] = -inf
    
    for i in range(len(vals) - 2, -1, -1):
        dp[0][i] = max(vals[i] + dp[0][i + 1], vals[i] + dp[1][i + 1])
        dp[1][i] = max(-vals[i] -vals[i + 1] + dp[0][i + 1] - vals[i + 1], -vals[i] + vals[i + 1] + dp[1][i + 1] + vals[i + 1])
        
    print(max(dp[0][0], dp[1][0]))