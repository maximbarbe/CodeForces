n = int(input())
res= 0
for i in range(n):
    row = input().split()
    if row.count('1') >= 2:
        res += 1
print(res)