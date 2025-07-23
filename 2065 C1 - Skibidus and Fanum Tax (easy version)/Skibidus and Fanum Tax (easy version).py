import heapq

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    maximum = [(1, -1)]
    vals = [*map(int, input().split())]
    s = int(input())
    dp = [[False for i in range(n)] for j in range(2)]
    dp[0][0] = True
    dp[1][0] = True
    for i in range(1, n):
        dp[0][i] = (vals[i] >= vals[i - 1] and dp[0][i - 1]) or (vals[i] >= s - vals[i - 1] and dp[1][i - 1])
        dp[1][i] = (s - vals[i] >= vals[i - 1] and dp[0][i - 1]) or (s - vals[i] >= s - vals[i - 1] and dp[1][i - 1])
    print(("NO","YES")[dp[0][-1] or dp[1][-1]])