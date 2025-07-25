from itertools import product


def can(a,b,c):
    return a + b > c and a + c > b and b + c > a

seen = dict()

t = int(input())
for i in range(t):
    x = int(input())
    if seen.get(x, None) != None:
        print(seen[x])
        continue
    for i in range(1, len(bin(x)[2:])):
        y = int("".join("1"*i), 2)
        if can(x, y, x^y):
            seen[x] = y
            print(y)
            break
    else:
        seen[x] = -1
        print(-1)