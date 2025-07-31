t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    if l == r:
        if l == 1:
            print(1)
        else:
            print(0)
    else:
        print(r - l)