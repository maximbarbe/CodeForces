n, m = map(int, input().split())
prev = None
for i in range(n):
    row = input()
    char = set(row)
    if len(char) > 1 or char == prev:
        print("NO")
        exit()
    else:
        prev = char
else:
    print("YES")