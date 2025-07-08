n, q = map(int, input().split())
cards = dict()
vals = [*map(int, input().split())]
queries = [*map(int, input().split())]
for i, v in enumerate(vals):
    if cards.get(v) == None:
        cards[v] = i + 1
res = []  
for q in queries:
    idx = cards[q]
    res.append(idx)
    cards[q] = 1
    if idx != 1:
        for key, val in cards.items():
            if key != q and val < idx:
                cards[key] += 1
print(*res)
                