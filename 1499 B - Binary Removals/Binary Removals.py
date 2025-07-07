t = int(input())
for i in range(t):
    s = input() + "11"
    dp = [[False for j in range(len(s))] for k in range(2)]
    dp[0][-1] = True
    dp[1][-1] = True
    dp[0][-2] = True
    dp[1][-2] = True
    for i in range(len(s) - 3, -1, -1):
        
        # dp[0][i], on garde le caractère i
        
        dp[0][i] = (s[i] <= s[i + 1] and dp[0][i + 1]) or (s[i] <= s[i + 2] and dp[1][i + 1])
        
        # dp[1][i], on ne garde pas le caractère i
        dp[1][i] = dp[0][i + 1]
        
        
        
    if dp[0][0] or dp[0][1]:
        print("YES")
    else:
        print("NO")