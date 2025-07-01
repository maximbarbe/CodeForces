from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    if len(vals) < 3:
        print(-1)
    else:
        for i in range(len(vals) - 2):
            if vals[i] == vals[i + 1] and vals[i + 1] == vals[i + 2]:
                print(vals[i])
                break
        else:
            print(-1)