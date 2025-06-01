n = int(input())
res = 0
f = input()
s = input()
for i in range(len(f)):
    first = int(f[i])
    sec = int(s[i])
    res += min(abs(sec - first), abs(first - sec), abs(sec + 10 - first), abs(first + 10 - sec))
print(res)