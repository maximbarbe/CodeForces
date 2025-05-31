rectangles = []
while True:
    line = input()
    if line == "*":
        break
    else:
        _, x1, y1, x2, y2 = line.split()
        x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
        rectangles.append((x1, y1, x2, y2))

p = 0
while True:
    p += 1
    x, y = map(float, input().split())
    if x == y == 9999.9:
        break
    figures = []
    for i, (x1, y1, x2, y2) in enumerate(rectangles):
        if x <= x1 or x >= x2 or y >= y1 or y <= y2:
            continue
        else:
            figures.append(i + 1)
    if not figures:
        print("Point " + str(p) + " is not contained in any figure")
    else:
        for fig in figures:
            print("Point " + str(p) + " is contained in figure " + str(fig))