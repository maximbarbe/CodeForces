t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    res = ["B"]*m
    vals = [*map(int, input().split())]
    for v in vals: 
        if v - 1 < m - v:
            if res[v - 1] == "B":
                res[v - 1] = "A"
            else:
                res[m - v] = "A"
        else:
            if res[m - v] == "B":
                res[m - v] = "A"
            else:
                res[v - 1] = "A"
    print("".join(res))