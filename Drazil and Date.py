a,b,s = map(int, input().split())
distance = abs(a) + abs(b)
if distance > s or (s - distance)%2 != 0:
    print("No")
else:
    print("Yes")