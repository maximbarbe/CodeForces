vp = int(input())
vd = int(input())
t = int(input())
f = int(input())
c = int(input())
initial_distance = t * vp
res = 0
cur = 0
if initial_distance >= c:
    print(0)
    exit()
while True:
    
    
    
    if initial_distance >= c:
        print(res)
        exit()
    initial_distance += vp
    cur += vd
    if cur < initial_distance:
        continue
    else:
        initial_distance -= vp
        cur -= vd
        k = (cur-initial_distance)/(vp-vd)
        
        intersecting_point = cur + k*vd
        
        if intersecting_point < c:
            res += 1
            initial_distance = intersecting_point + (intersecting_point/vd)*vp + f*vp
            cur = 0
        else:
            print(res)
            exit()
            continue