t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    odds = []
    evens = []
    for i, v in enumerate(vals):
        if v%2 == 0:
            evens.append(i + 1)
        else:
            odds.append(i + 1)
    if len(odds)%2 == 1:
        odds.pop()
        evens.pop()
    else:
        if odds:
            odds.pop()
            odds.pop()
        else:
            evens.pop()
            evens.pop()
    for i in range(0, len(odds), 2):
        print(odds[i], odds[i + 1])
    for i in range(0, len(evens), 2):
        print(evens[i], evens[i + 1])