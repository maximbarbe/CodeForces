t = int(input())
for i in range(t):
    vals = [*map(int, input().split())]
    res = 0
    while vals != [0, 0, 0]:
        vals.sort()
        if vals[-1] % 2 == 1 and vals[-2] == 0:
            print(-1)
            break
        else:
            if vals[-2] == 0:
                vals[-1] = 0
            else:
                vals[-1] -= 1
                vals[-2] -= 1
                res += 1
    else:
        print(res)