input()
a_s = [*map(int, input().split())]
input()
b_s = [*map(int, input().split())]
max_ratio = 0
res = 0
for a in a_s:
    for b in b_s:
        ratio = b/a
        if ratio == int(ratio):
            if ratio > max_ratio:
                max_ratio = int(ratio)
                res = 1
            elif ratio == max_ratio:
                res += 1
print(res)