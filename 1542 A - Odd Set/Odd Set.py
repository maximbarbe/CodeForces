t = int(input())
for i in range(t):
    input()
    vals = [*map(int, input().split())]
    odds = 0
    pairs = 0
    for v in vals:
        if v % 2 == 1:
            odds += 1
        else:
            pairs += 1
    print("Yes" if pairs == odds else 'No')