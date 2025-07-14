t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    s = input()
    ss = sorted([char for char in s])
    for i in range(n):
        if s[i] == ss[i]:
            res += 1
    print(n-res)