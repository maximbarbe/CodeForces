input()
vals = [*map(int, input().split())]
d =  {
    0: [],
    1: []
}
for i, v in enumerate(vals):
    d[v % 2].append(i)
if len(d[0]) == 1:
    print(d[0][0] + 1)
else:
    print(d[1][0] + 1)