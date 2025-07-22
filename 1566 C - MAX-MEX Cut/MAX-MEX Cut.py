t = int(input())
for i in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    res = 0
    zeros = False
    ones = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if zeros:
                res += 1
            res += 2
            ones = False
            zeros = False
        else:
            if c1 == "0":
                if ones:
                    res += 2
                    zeros = False
                    ones = False
                else:
                    if zeros:
                        res += 1
                    else:
                        zeros = True
            else:
                if zeros:
                    res += 2
                    ones = False
                    zeros = False
                else:
                    ones = True
    if zeros:
        res += 1
    print(res)