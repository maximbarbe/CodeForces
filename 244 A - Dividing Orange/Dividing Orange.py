n, k = map(int, input().split())
taken = {i:False for i in range(1, n*k + 1)}
wanted = [*map(int, input().split())]
oranges = [[] for i in range(k)]
for i in range(len(wanted)):
    oranges[i].append(wanted[i])
    taken[wanted[i]] = True
idx = 0
for i in range(1, n*k+1):
    while idx != k and len(oranges[idx]) == n:
        idx += 1
    if taken[i]:
        continue
    oranges[idx].append(i)
for c in oranges:
    print(*c)