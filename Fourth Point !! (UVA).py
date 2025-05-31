while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    except:
        break
    if x1 == x3 and y1 == y3:
        x1, y1, x2, y2 = x2, y2, x1, y1
    elif x1 == x4 and y1 == y4:
        x3, y3, x4, y4 = x4,y4,x3,y3
        x1,y1,x2,y2 = x2,y2,x1,y1
    elif x2 == x4 and y2 == y4:
        x3, y3, x4, y4 = x4,y4,x3,y3
    v = (x2-x1, y2-y1)
    print("{0:.3f}".format(x4 - v[0]), "{0:.3f}".format(y4-v[1]))