t = int(input())
for i in range(t):
    stack = []
    s = input()
    n = len(s)
    left = s.index("(")
    right = s.index(")")
    if s.count("?")%2 == 1 or right == 0 or left == len(s ) -1:
        print("NO")
    else:
        print("YES")
                