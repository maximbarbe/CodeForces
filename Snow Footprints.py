n = int(input())
path = input()

if "R" not in path:
    end = path.index("L")
    for i in range(n-1,-1,-1):
        if path[i] == "L":
            print(i + 1, end)
            exit()
elif "L" not in path:
    start = path.index("R") + 1
    for i in range(n-1,-1,-1):
        if path[i] == "R":
            print(start, i + 2)
            exit()
else:
    print(path.index("R") + 1, path.index("L"))