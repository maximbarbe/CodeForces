t = int(input())
for i in range(t):
    n = int(input())
    vals = set([*map(int, input().split())])
    print(len(vals))