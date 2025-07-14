t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if n == 1:
        print("YES")
    elif n == 2:
        if s[0] != s[1]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")