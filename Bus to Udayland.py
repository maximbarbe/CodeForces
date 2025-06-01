n = int(input())
rows = []
for i in range(n):
    rows.append(input().split("|"))
found = False
for i in range(n):
    for j in range(2):
        if rows[i][j] == "OO":
            rows[i][j] = "++"
            found=True
            break
    if found:
        break
if found:
    print("YES")
    for a, b in rows:
        print("|".join([a, b]))
else:
    print("NO")
