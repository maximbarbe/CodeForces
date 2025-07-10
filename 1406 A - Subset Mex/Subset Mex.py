t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    left = set()
    right = set()
    for v in vals:
        if v in left:
            right.add(v)
        else:
            left.add(v)
    a = 0
    b = 0
    cur = 0
    while cur in left:
        cur += 1
    a = cur
    cur = 0
    while cur in right:
        cur += 1
    b = cur
    print(a + b)