from collections import defaultdict, deque

t = int(input())
for i in range(t):
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    if (xa, ya) == (xb, yb):
        print(0)
    else:
        if xa == xb:
            if xf == xa and min(ya, yb) <= yf <= max(ya, yb):
                print(abs(xa - xb) + abs(ya -yb) + 2)
            else:
                print(abs(xa - xb) + abs(ya -yb))
        elif ya == yb:
            if yf == ya and min(xa, xb) <= xf <= max(xa, xb):
                print(abs(xa - xb) + abs(ya -yb) + 2)
            else:
                print(abs(xa - xb) + abs(ya -yb))
        else:
            print(abs(xa - xb) + abs(ya -yb))