t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    words = []
    for i in range(n):
        words.append(input())
    res = 10**6
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            cur = 0
            for k in range(m):
                c1 = ord(words[i][k])
                c2 = ord(words[j][k])
                cur += abs(c2 -c1)
            res = min(cur, res)
    print(res)