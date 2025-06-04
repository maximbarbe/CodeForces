ms = [*map(int, input().split())]
ws = [*map(int, input().split())]
xs = [500, 1000, 1500, 2000, 2500]
hs, hu = map(int, input().split())
res = 0
for i in range(5):
    res += max(0.3*xs[i], (1-ms[i]/250)*xs[i] - 50*ws[i])

res += 100*hs - 50*hu
print(int(res))