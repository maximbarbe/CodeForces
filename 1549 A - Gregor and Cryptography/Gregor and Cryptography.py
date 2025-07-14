t = int(input())
for i in range(t):
    p = int(input())
    seen = dict()
    cur = 2
    while True:
        if seen.get(p%cur, None) != None:
            print(seen[p%cur], cur)
            break
        else:
            seen[p%cur] = cur
        cur += 1