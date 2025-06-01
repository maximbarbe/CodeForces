n = input()
res = 0
for c in n:
    if c in "47":
        res += 1
res = str(res)
for c in res:
    if c not in "47":
        print("NO")
        exit()
else:
    print("YES")