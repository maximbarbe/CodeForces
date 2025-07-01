t = int(input())
for i in range(t):
    input()
    vals = [*map(int, input().split())]
    cur = 0
    longest = 0
    for v in vals:
        if v == 0:
            cur += 1
        else:
            cur = 0
        if cur > longest:
            longest = cur
    print(longest)