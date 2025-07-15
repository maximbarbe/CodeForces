def res(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return "TRIANGLE"
    elif a + b >= c and a + c >= b and b + c >= a:
        return "SEGMENT"
    else:
        return "IMPOSSIBLE"
    
s = False    
lengths = [*map(int, input().split())]
for i in range(len(lengths) - 2):
    for j in range(i +1,len(lengths) - 1):
        for k in range(j + 1, len(lengths)):
            r = res(lengths[i], lengths[j], lengths[k])
            if r[0] == "T":
                print("TRIANGLE")
                exit()
            elif r[0] == "S":
                s = True
if s:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
            