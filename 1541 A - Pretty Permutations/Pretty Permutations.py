t = int(input())
for i in range(t):
    v = [j for j in range(1, int(input()) + 1)]
    if len(v) % 2 == 0:
        for i in range(0, len(v), 2):
            v[i], v[i+1] = v[i + 1], v[i]
    else:
        for i in range(0, len(v) - 1, 2):
            v[i], v[i+1] = v[i + 1], v[i]
        v[-1], v[-2] = v[-2], v[-1]
    print(*v)