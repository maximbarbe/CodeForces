k, r = map(int, input().split())
res = 1
cur = k
while (cur % 10) != 0 and (cur % 10) - r != 0:
    cur += k
    res += 1
print(res)