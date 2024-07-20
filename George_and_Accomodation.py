n = int(input())
res = 0
for i in range(n):
    pi, qi = map(int, input().split())
    if qi - pi >= 2:
        res += 1
print(res)