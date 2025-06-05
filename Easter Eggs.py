n = int(input())
s = "ROYGBIV"
res = s
for i in range(n-7):
    res += res[-4]
print(res)