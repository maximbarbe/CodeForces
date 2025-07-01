from math import pi

d,h,v,e = map(int, input().split())
initial_volume_ml = (d/2)**2*pi*h
growth_rate = e*(d/2)**2*pi

if growth_rate >= v:
    print("NO")
else:
    print("YES")
    print(-initial_volume_ml/(-v + growth_rate))