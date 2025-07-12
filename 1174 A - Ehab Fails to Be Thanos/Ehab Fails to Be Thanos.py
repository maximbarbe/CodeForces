n = int(input())
v = [*map(int, input().split())]
if len(set(v)) == 1:
    print(-1)
else:
    print(*sorted(v))