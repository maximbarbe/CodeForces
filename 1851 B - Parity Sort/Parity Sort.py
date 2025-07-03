from collections import defaultdict

n = int(input())
for i in range(n):
    input()
    vals = [*map(int, input().split())]
    odds = dict()
    for i in range(len(vals)):
        odds[i] = vals[i] %2
    vals.sort()
    for i in range(len(vals)):
        if odds[i] % 2 != vals[i] % 2:
            print("NO")
            break
    else:
        print('YES')