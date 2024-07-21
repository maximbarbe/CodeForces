vect = [0, 0,0]
t = int(input())
for i in range(t):
    x1,x2,x3 = map(int, input().split())
    vect[0] += x1
    vect[1] += x2
    vect[2] += x3
    
if vect == [0,0,0]:
    print("YES")
else:
    print("NO")