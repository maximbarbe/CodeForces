from bisect import bisect_left
n, m, k, t = map(int, input().split())
waste = []
for i in range(k):
    a, b = map(lambda el:int(el) - 1, input().split())
    waste.append(a*m + b)
res = ["Carrots", "Kiwis", "Grapes"]
waste.sort()
for i in range(t):
    i, j =map(lambda el:int(el) - 1, input().split())
    pos = i*m + j
    idx = bisect_left(waste, pos)
    if idx != k:
        if waste[idx] == pos:
            print("Waste")
        else:
            pos -= idx
            print(res[pos%3])
    else:
        print(res[(pos-k)%3])
