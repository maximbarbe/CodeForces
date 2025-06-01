from math import ceil
n, x = map(int, input().split())
s = abs(sum([*map(int, input().split())]))
print(ceil(s/x))