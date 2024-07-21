string = input()
to_find = "hello"
cur = 0
for i in range(len(string)):
    if string[i] == to_find[cur]:
        cur += 1
    if cur == 5:
        print("YES")
        exit()
else:
    print("NO")
