res = False
n = int(input())
for i in range(n):
    _, a, b = input().split()
    if int(a) >= 2400 and int(b) > int(a):
        res = True
if res:
    print("YES")
else:
    print("NO")