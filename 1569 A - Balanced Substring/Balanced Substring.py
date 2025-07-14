t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    for i in range(n - 1):
        if s[i] == "a" and s[i + 1] == "b" or s[i] == "b" and s[i + 1] == "a":
            print(i + 1, i + 2)
            break
    else:
        print(-1, -1)