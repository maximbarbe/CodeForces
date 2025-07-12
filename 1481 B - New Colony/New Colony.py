t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    heights = [*map(int, input().split())]
    res = []
    while True:
        for i in range(len(heights) - 1):
            if heights[i] < heights[i + 1]:
                res.append(i + 1)
                heights[i] += 1
                break
        else:
            break
    if k > len(res):
        print(-1)
    else:
        print(res[k - 1])