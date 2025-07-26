from bisect import bisect_right
n, m = map(int, input().split())
a = sorted([*map(int, input().split())])
b = [*map(int, input().split())]
print(*[bisect_right(a, v) for v in b])