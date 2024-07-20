k, n, w = map(int, input().split())
cost = 0

for i in range(1, w + 1):
    cost += k*i
print(max(0, cost - n))