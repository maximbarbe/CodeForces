from functools import lru_cache


@lru_cache(None)
def res(n):
    if n in [0, 1]:
        return 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] <= n:
            return 1 + res(n - heights[i])
        
    return 0


heights = [2]
h = 2
while (v := heights[-1] + 3*h - 1) <= 10**9:
    heights.append(v)
    h += 1

t = int(input())
for i in range(t):
    print(res(int(input())))