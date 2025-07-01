res = 0
n = int(input())
for i in range(1, n):
    if n % i == 0:
        res += 1
print(res)