n, a = map(int, input().split())
t = [*map(int, input().split())]
a -= 1
res = 0
for i in range(n):
    if i == 0:
        if t[a + i] == 1:
            res += 1
    else:
        if a - i >= 0 and a + i <= n-1:
            if t[a-i]==1 and t[a + i] == 1:
                res += 2
        elif a - i < 0 and a +i<=n-1:
            if t[a + i] == 1:
                res += 1
        elif a - i >= 0 and a + i > n-1:
            if t[a - i] == 1:
                res += 1
print(res)