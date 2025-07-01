from collections import defaultdict
from math import dist

keyboard = defaultdict(lambda:[])
n,m,x = map(int, input().split())
for i in range(n):
    row = input()
    for j in range(m):
        keyboard[row[j]].append((i, j))
res = 0
n = int(input())
string = input()
seen = dict()
for c in string:
    if seen.get(c) != None:
        res += seen[c]
        continue
    if c.isupper():
        if not keyboard[c.lower()] or not keyboard["S"]:
            print(-1)
            exit()
        else:
            temp = c.lower()
            found = False
            for p1 in keyboard[temp]:
                
                for p2 in keyboard["S"]:
                    if dist(p1, p2) <= x:
                        break
                else:
                    continue
                seen[c] = 0
                break
            else:
                seen[c] = 1
                res += 1
    else:
        if not keyboard[c.lower()]:
            print(-1)
            exit()
        seen[c] = 0
print(res)