t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    dp = [0]*n
    for i in range(len(vals) - 1, -1, -1):
        if i + vals[i] >= n:
            dp[i] = vals[i]
        else:
            dp[i] = vals[i] + dp[i + vals[i]]
    print(max(dp))