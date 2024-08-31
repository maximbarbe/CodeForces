n, m = map(int, input().split())
vals = list(filter(lambda x: x <= 0, [*map(int, input().split())]))
if len(vals) == 0:
    print(0)
elif len(vals) < m:
    print(-1 * sum(vals))
else:
    print(-1 * sum(sorted(vals)[:m]))
