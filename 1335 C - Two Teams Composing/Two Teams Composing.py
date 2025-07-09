from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    c = Counter(vals)
    if n == 1:
        print(0)
    else:
        distinct = set(vals)
        char, max_freq = c.most_common(1)[0]
        seen = dict()
        left = []
        right = []
        for v in vals:
            if v == char:
                right.append(v)
            else:
                if not seen.get(v, False):
                    left.append(v)
                    seen[v] = True
        if len(left) >= len(right):
            print(len(right))
        else:
            if len(right) - len(left) >= 2:
                print(len(left) + 1)
            else:
                print(len(left))