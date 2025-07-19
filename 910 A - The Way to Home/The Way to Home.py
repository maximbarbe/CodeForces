n, d = map(int, input().split())
s = input()
dp = [10**6] * n
dp[-1] = 0
for i in range(n-2, -1, -1):
    if s[i] == "1":
        for j in range(i + 1, min(n, i + d + 1)):
            dp[i] = min(dp[i], 1 + dp[j])
    
print((-1,dp[i])[dp[i] != 10**6])