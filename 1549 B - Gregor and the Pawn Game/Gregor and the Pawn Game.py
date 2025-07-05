t = int(input())
for i in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    res = 0
    taken = [False]*n
    for i in range(n):
        if s2[i] == "1":
            if s1[i] == "0":
                res += 1
                taken[i] = True
            else:
                if i == 0:
                    if s1[i + 1] == "1":
                        res += 1
                        taken[i + 1] = True
                elif i == n - 1:
                    if s1[i - 1] == "1" and not taken[i - 1]:
                        res += 1
                        taken[i - 1] = True
                else:
                    if s1[i - 1] == "1" and not taken[i - 1]:
                        res += 1
                        taken[i - 1] = True
                    elif s1[i + 1] == "1":
                        res += 1
                        taken[i + 1] = True
    print(res)