t = int(input())
for i in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    for i in range(len(s1)):
        if (s1[i] == "G" or s1[i] == "B") and s2[i] not in "GB":
            print("NO")
            break
        elif s1[i] == "R" and s2[i] != "R" or s2[i] == "R" and s1[i] != "R":
            print("NO")
            break
    else:
        print('YES')