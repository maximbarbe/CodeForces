t = int(input())
for i in range(t):
    n = int(input())
    dp = [[False for j in range(n + 1)] for i in range(2)]
    vals = [*map(int, input().split())]
    for i in range(len(vals) - 1, -1, -1):
        if vals[i] == 1:
            dp[0][i] = not dp[1][i + 1]
            dp[1][i] = not dp[0][i + 1]
        else:
            dp[0][i] = not dp[1][i + 1] or dp[0][i + 1]
            dp[1][i] = dp[1][i + 1] or not dp[0][i + 1]
    if dp[0][0]:
        print("First")
    else:
        print("Second")