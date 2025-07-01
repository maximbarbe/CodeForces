t = int(input())
for _ in range(t):
    s = input()
    char = input()
    for j, c in enumerate(s):
        if c == char and j % 2 == 0:
            print("YES")
            break
    else:
        print("NO")