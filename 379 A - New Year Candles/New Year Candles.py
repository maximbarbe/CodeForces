a, b = map(int, input().split())
res = a
cur = a
while cur // b != 0:
    res += cur //b
    cur = cur % b + cur//b
print(res)