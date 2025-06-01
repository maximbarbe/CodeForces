a, b = map(int, input().split())
first = draw = sec = 0
for i in range(1, 7):
    if abs(i - a) < abs(i - b):
        first += 1
    elif abs(i - a) > abs(i - b):
        sec += 1
    else:
        draw += 1
print(first, draw, sec)