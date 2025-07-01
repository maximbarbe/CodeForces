n = int(input())
dice = set()
up_face = int(input())
prev_down_face = None
found = False
for i in range(n):
    a, b = map(int, input().split())
    dice.add(a)
    dice.add(b)
    dice.add(7-a)
    dice.add(7-b)
    if i == 0:
        prev_down_face = 7 - up_face
    else:
        if prev_down_face in dice and not found:
            print("NO")
            found = True
if not found:
    print("YES")
