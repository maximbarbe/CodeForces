t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    evens = 0
    odds = 0
    for i, v in enumerate(vals):
        if v % 2 != i % 2:
            if v % 2 == 1:
                odds += 1
            else:
                evens += 1
    if odds != evens:
        print(-1)
    else:
        print(odds)