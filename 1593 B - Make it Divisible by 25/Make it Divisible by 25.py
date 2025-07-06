t = int(input())
for i in range(t):
    n = int(input())
    digits = [int(c) for c in str(n)]
    cur = 0
    while digits[-1] not in [0, 5]:
        digits.pop()
        cur += 1
    digits = digits[::-1]

    minimum = 19
    first = None
    second = None
    for j, d in enumerate(digits):
        if d == 0:
            if first == None:
                first = j
            else:
                second = j
                break
    if first != None and second != None:
        minimum = min(minimum, first + (second - first - 1))
    first = None
    second = None
    for j, d in enumerate(digits):
        if d == 5:
            if first == None:
                first = j
        elif d == 2:
            if first != None:
                second = j
                break
    if first != None and second != None:
        minimum = min(minimum, first + (second - first - 1))
    first = None
    second = None
    for j, d in enumerate(digits):
        if d == 5:
            if first == None:
                first = j
        elif d == 7:
            if first != None:
                second = j
                break
    if first != None and second != None:
        minimum = min(minimum, first + (second - first - 1))
    first = None
    second = None
    for j, d in enumerate(digits):
        if d == 0:
            if first == None:
                first = j
        elif d == 5:
            if first != None:
                second = j
                break
    if first != None and second != None:
        minimum = min(minimum, first + (second - first - 1))
    
    print(minimum + cur)