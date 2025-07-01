n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
a_s = 0
bs = 0
for ai, bi in zip(a, b):
    a_s |= ai
    bs |= bi
print(a_s + bs)
    