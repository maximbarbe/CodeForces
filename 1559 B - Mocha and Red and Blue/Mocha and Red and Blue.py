t =int(input())
for i in range(t):
    n = int(input())
    s = input()
    s1 = [c for c in s]
    s2 = s1.copy() + ["R"]
    s1 = s1 + ["B"]
    for i in range(len(s1)):
        if s1[i] != "?":
            left = i - 1
            right = i + 1
            prev = s1[i]
            while left != -1 and s1[left] == "?":
                if prev == "B":
                    s1[left] = "R"
                    prev = "R"
                else:
                    s1[left] = "B"
                    prev = "B"
                left -= 1
            prev = s1[i]
            while right != len(s1) and s1[right] == "?":
                if prev == "B":
                    s1[right] = "R"
                    prev = "R"
                else:
                    s1[right] = "B"
                    prev = "B"
                right += 1
    for i in range(len(s2)):
        if s2[i] != "?":
            left = i - 1
            right = i + 1
            prev = s2[i]
            while left != -1 and s2[left] == "?":
                if prev == "B":
                    s2[left] = "R"
                    prev = "R"
                else:
                    s2[left] = "B"
                    prev = "B"
                left -= 1
            prev = s2[i]
            while right != len(s2) and s2[right] == "?":
                if prev == "B":
                    s2[right] = "R"
                    prev = "R"
                else:
                    s2[right] = "B"
                    prev = "B"
                right += 1
    c1 = 0
    c2 = 0
    for i in range(len(s1) - 2):
        if s1[i] == s1[i + 1]:
            c1 += 1
    for i in range(len(s2) - 2):
        if s2[i] == s2[i + 1]:
            c2 += 1
    if c1 <= c2:
        print("".join(s1[:-1]))
    else:
        print("".join(s2[:-1]))
            