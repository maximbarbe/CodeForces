from math import ceil

t = int(input())
for i in range(t):
    r, b, d = map(int, input().split())
    packets = min(r, b)
    maximum = ceil(max(r, b)/packets)
    if maximum - 1 > d:
        print("NO")
    else:
        print("YES")