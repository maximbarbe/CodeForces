
def split(n):
    res = []
    while n != 0:
        res.append(n%10)
        n//=10
    res = res[::-1]
    if not res:
        return [0]
    return res

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    dp = [[False for i in range(n)] for j in range(2)]
    dp[0][-1] = True
    s = split(vals[-1])
    dp[1][-1] = s == sorted(s)
    for i in range(n-2, -1, -1):
        dp[0][i] = vals[i] <= vals[i + 1] and dp[0][i + 1]
        s1 = split(vals[i])
        s2 = split(vals[i + 1])
        dp[1][i] = s1 == sorted(s1) and (s1[-1] <= vals[i + 1] and dp[0][i + 1] or s1[-1] <= s2[0] and dp[1][i + 1])
    print(("NO","YES")[dp[0][0] or dp[1][0]])