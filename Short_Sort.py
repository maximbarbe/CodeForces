answers = set(["abc", "acb", "bac", "cba"])
t = int(input())
for i in range(t):
    if input() in answers:
        print("YES")
    else:
        print("NO")