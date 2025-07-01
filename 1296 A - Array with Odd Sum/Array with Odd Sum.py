t = int(input())
for _ in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    odds = 0
    evens = 0
    for v in vals:
        if v % 2 == 0:
            evens += 1
        else:
            odds += 1
    if odds == 0:
        print("NO")
    else:
        if n % 2 == 1:
            print("YES")
        else:
            if odds != len(vals):
                print("YES")
            else:
                print("NO")