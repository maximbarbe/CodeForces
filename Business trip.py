k = int(input())
vals = sorted([*map(int, input().split())], reverse=True)
if k == 0:
    print(0)
    exit()
for i in range(1, 13):
    k -= vals[i - 1]
    if k <= 0:
        print(i)
        exit()
else:
    print(-1)