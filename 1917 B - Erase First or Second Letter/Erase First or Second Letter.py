n = int(input())
for i in range(n):
    l = input()
    s = input()
    dp = [0]*(len(s))
    next = [len(s)]*26
    next[ord(s[-1]) - ord('a')] = len(s) - 1
    dp[-1] = 1
    for i in range(len(s) -2, -1, -1):
        dp[i] = dp[i + 1] + next[ord(s[i]) - ord('a')] - i
        next[ord(s[i]) - ord('a')] = i
            
    print(dp[0])