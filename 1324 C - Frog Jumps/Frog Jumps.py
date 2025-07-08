t = int(input())
for i in range(t):
    s = input()
    pos = []
    for i in range(len(s)):
        if s[i] == "R":
            pos.append(i + 1)
        
    if not pos:
        print(len(s) + 1)
    else:
        res = 0
        pos = [0] + pos + [len(s) + 1]
        for i in range(1, len(pos) - 1):
            res = max(res, pos[i] - pos[i - 1], pos[i + 1] - pos[i])
        print(res)
        