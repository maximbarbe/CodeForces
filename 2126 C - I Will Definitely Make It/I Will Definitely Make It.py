t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    k -= 1
    heights = [*map(int, input().split())]
    cur = heights[k]
    heights.sort()
    water = 1
    time = 0
    idx = heights.index(cur)
    while idx != n - 1:
        arrival = time + heights[idx + 1] - heights[idx]
        if heights[idx] < water + heights[idx + 1] - heights[idx] - 1:
            print("NO")
            break
        else:
            water = water + arrival - time
            time = arrival
            idx += 1
    else:
        print("YES")