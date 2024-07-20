letters = set("codeforces")
t = int(input())
for i in range(t):
    if input() in letters:
        print("YES")
    else:
        print('NO')