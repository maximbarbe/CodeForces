n = int(input())
laptops = []
for i in range(n):
    a, b = map(int, input().split())
    laptops.append((a, b))
laptops.sort(key=lambda el:(el[0], -el[1]))
cur_price = laptops[0][0]
cur_quality = laptops[0][1]
for a, b in laptops[1:]:
    if a == cur_price:
        if b > cur_quality:
            cur_quality = b
    elif a > cur_price:
        if cur_quality > b:
            print("Happy Alex")
            exit()
        elif b > cur_quality:
            cur_price = a
            cur_quality = b
else:
    print("Poor Alex")