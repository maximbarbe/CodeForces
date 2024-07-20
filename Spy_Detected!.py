from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    indices = defaultdict(lambda:[])
    for idx, val in enumerate(vals):
        indices[val].append(idx)
    for key in indices.keys():
        if len(indices[key]) == 1:
            print(indices[key][0] + 1)
            break
    