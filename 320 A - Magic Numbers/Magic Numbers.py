s = input()
idx = 0
while idx != len(s):
    if idx + 2 < len(s) and s[idx:idx + 3] == "144":
        idx += 3
    elif idx + 1 < len(s) and s[idx:idx + 2] == "14":
        idx += 2
    elif s[idx] == "1":
        idx += 1
    else:
        print("NO")
        exit()
print("YES")