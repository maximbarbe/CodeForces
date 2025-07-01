vals = [*map(int, input().split())]
res = 0
for char in input():
    res += vals[int(char) - 1]
print(res)