res = 0
n = int(input())
cur = 0
for i in range(n):
    left, arrived = map(int, input().split())
    cur -= left
    cur += arrived
    res = max(cur, res)
print(res)