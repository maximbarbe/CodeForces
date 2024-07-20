n, k = map(int, input().split())
vals = [0]
for i in range(1, n + 1):
    vals.append(5 * i + vals[i - 1])
time = 240 - k

if time < 5:
    print(0)
else:
    for i in range(len(vals) - 1, 0, -1):
        if vals[i] <= time:
            print(i)
            exit()