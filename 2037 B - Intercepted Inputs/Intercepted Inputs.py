for i in range(int(input())):
    k = int(input())
    vals = [*map(int, input().split())]
    seen = dict()
    for v in vals:
        if (k - 2)%v == 0:
            if seen.get(v, None) != None:
                print(v, seen[v])
                break
            seen[(k-2)//v] = v