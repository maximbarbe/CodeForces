t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    odds = 0
    evens = 0
    for v in vals:
        if v % 2 ==0:
            evens += v
        else:
            odds += v
    if evens > odds:
        print("YES")
    else:
        print("NO")