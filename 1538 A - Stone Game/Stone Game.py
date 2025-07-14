from collections import deque

t = int(input())
for i in range(t):
    n = int(input())
    vals = deque([*map(int, input().split())])
    min_idx = vals.index(min(vals))
    max_idx = vals.index(max(vals))
    min_moves_left = min_idx + 1
    min_moves_right = n - min_idx
    max_moves_left = max_idx + 1
    max_moves_right = n - max_idx
    res= 0
    if min(min_moves_left, min_moves_right) <= min(max_moves_left, max_moves_right):
        if min_moves_left <= min_moves_right:
            res += min_moves_left
            for i in range(min_moves_left):
                vals.popleft()
        else:
            res += min_moves_right
            for i in range(min_moves_right):
                vals.pop()
        max_idx = vals.index(max(vals))
        max_moves_left = max_idx + 1
        max_moves_right = len(vals) - max_idx
        res += min(max_moves_right, max_moves_left)
    else:
        if max_moves_left <= max_moves_right:
            res += max_moves_left
            for i in range(max_moves_left):
                vals.popleft()
        else:
            res += max_moves_right
            for i in range(max_moves_right):
                vals.pop()
        min_idx = vals.index(min(vals))
        min_moves_left = min_idx + 1
        min_moves_right = len(vals) - min_idx
        res += min(min_moves_left, min_moves_right)
    print(res)