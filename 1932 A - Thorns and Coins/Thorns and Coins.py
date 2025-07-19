t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    dp = [0]*(n + 2)
    for i in range(n - 1, -1, -1):
        if s[i] == "*":
            continue
        else:
            coin = s[i] == "@"
            dp[i] = coin + max(dp[i + 1], dp[i + 2])
    print(dp[0])