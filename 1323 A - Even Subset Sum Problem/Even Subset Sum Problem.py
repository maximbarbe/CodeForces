t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    evens = []
    odds = []
    for j in range(len(vals)):
        if vals[j]%2 == 0:
            evens.append(j + 1)
        else:
            odds.append(j + 1)
    if evens:
        print(1)
        print(evens[0])
    else:
        if len(odds) == 1:
            print(-1)
        else:
            print(2)
            print(odds[0], odds[1])