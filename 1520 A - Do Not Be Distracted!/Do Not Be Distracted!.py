t = int(input())
for i in range(t):
    n = int(input())
    seen = dict()
    string = input()
    cur = None
    for j in range(n):
        if seen.get(string[j], False) == True and string[j] != cur:
            print("NO")
            break
        else:
            seen[string[j]] = True
            cur = string[j]
    else:
        print("YES")