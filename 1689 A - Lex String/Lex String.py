t = int(input())
for i in range(t):
    n,m,k = map(int, input().split())
    a = sorted([char for char in input()])
    b = sorted([char for char in input()])
    i = 0
    j = 0
    prev = None
    cur = 0
    res = []
    while i != len(a) and j != len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
            prev = None
            cur = 0
        elif a[i] < b[j]:
            if prev == "b":
                prev = "a"
                cur = 1
                res.append(a[i])
                i += 1
            else:
                if cur != k:
                    prev = "a"
                    cur += 1
                    res.append(a[i])
                    i += 1
                else:
                    prev = "b"
                    cur = 1
                    res.append(b[j])
                    j += 1
        else:
            if prev == "a":
                prev = "b"
                cur = 1
                res.append(b[j])
                j += 1
            else:
                if cur != k:
                    prev = "b"
                    cur += 1
                    res.append(b[j])
                    j += 1
                else:
                    prev = "a"
                    cur = 1
                    res.append(a[i])
                    i += 1
    print("".join(res))
            