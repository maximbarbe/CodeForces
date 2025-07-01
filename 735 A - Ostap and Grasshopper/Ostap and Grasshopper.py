n, k = map(int, input().split())
string = input()
start = string.index("G")
end = string.index("T")
if abs(start - end)%k != 0:
    print("NO")
    exit()
else:
    if start < end:
        for i in range(start, end+1, k):
            if string[i] == "#":
                print("NO")
                exit()
        print("YES")
    else:
        for i in range(start, end - 1, -k):
            if string[i] == "#":
                print("NO")
                exit()
        print("YES")