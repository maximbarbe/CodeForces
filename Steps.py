n, m = map(int, input().split())
xc,yc = map(int, input().split())
res = 0
for i in range(int(input())):
    dx, dy = map(int, input().split())
    if dx == 0:
        if dy < 0:
            steps = (yc - 1)//-dy
        else:
            steps = (m-yc)//dy
        res += steps
        yc += steps*dy            
    elif dy == 0:
        if dx < 0:
            steps = (xc - 1)//-dx
        else:
            steps = (n-xc)//dx
        res += steps
        xc += steps*dx  
    else:
        if dy < 0:
            stepsy = (yc - 1)//-dy
        else:
            stepsy = (m-yc)//dy
        if dx < 0:
            stepsx = (xc - 1)//-dx
        else:
            stepsx = (n-xc)//dx
        steps = min(stepsy, stepsx)
        res += steps
        xc += steps*dx
        yc += steps*dy
print(res)