t = int(input())
for i in range(t):
    n = int(input())
    min_diff = 10**9
    vals = [*map(int, input().split())]
    for i in range(len(vals) - 1):
        if vals[i + 1] - vals[i] < min_diff:
            min_diff = vals[i + 1] - vals[i]
    print(0 if min_diff < 0 else min_diff//2 + 1)