from random import shuffle

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    while True:
        indices = []
        for j in range(len(vals)):
            if vals[j] == (vals[(j - 1)%len(vals)] + vals[(j + 1)%len(vals)])/2:
                indices.append(j)
        if not indices:
            break
        shuffle(vals)
    print(*vals)