n =int(input())
res = ""
cur = 1
while len(res) < n:
    res += str(cur)
    cur += 1
print(res[n-1])