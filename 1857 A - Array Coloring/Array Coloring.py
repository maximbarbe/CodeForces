t = int(input())
for i in range(t):
    input()
    vals = [*map(int, input().split())]
    odds = 0
    for v in vals:
        if v % 2 == 1:
            odds += 1
    print('YES' if odds %2 == 0 else 'NO')