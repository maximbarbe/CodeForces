m, s = map(int, input().split())
if m == 1 and s == 0:
    print(0, 0)
    exit()
if s > m*9 or s == 0:
    print(-1, -1)
else:
    maximum= []
    cur = s
    for i in range(m):
        if cur >= 9:
            maximum.append(9)
            cur -= 9
        else:
            maximum.append(cur)
            cur = 0
            
    minimum = []
    cur = s
    for i in range(m):
        if i == m - 1:
            minimum.append(cur)
            continue
        for j in range(0, 10):
            if i == 0 and j == 0:
                continue
            if cur - j<= (m - i - 1) * 9:
                minimum.append(j)
                cur -= j
                break
                
    print("".join(map(str, minimum)), "".join(map(str, maximum)))
        