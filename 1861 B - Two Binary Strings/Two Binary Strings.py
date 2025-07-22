t = int(input())
for i in range(t):
    
    s1 = input()
    s2 = input()
    t1 = s1
    t2 = s2
    ones_1 = []
    z1 = []
    ones_2 = []
    z2 = []
    for j in range(len(s1)):
        if s1[j] == "1":
            ones_1.append(j)
        else:
            z1.append(j)
        if s2[j] == "1":
            ones_2.append(j)
        else:
            z2.append(j)
    i1 = 0
    i2 = 0
    found = False
    while i1 != len(ones_1) and i2 != len(ones_2):
        if ones_1[i1] == ones_2[i2]:

            if t1[ones_1[i1] - 1] == t2[ones_2[i2] - 1] == "0":
                print("YES")
                found = True
                break
            i1 += 1
            i2 += 1
        elif ones_1[i1] < ones_2[i2]:
            i1 += 1
        else:
            i2 += 1
    else:
        print("NO")
