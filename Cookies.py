t = int(input())
cookies = [*map(int, input().split())]
res = 0
s = sum(cookies)
for v in cookies:
    if (s - v)%2 == 0:
        res += 1
print(res)