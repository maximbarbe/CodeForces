t = int(input())
for i in range(t):
    a, b, c =map(int, input().split())

    maximum_value = max(a, b, c)
    count = 0
    if a == maximum_value:
        count += 1
    if b == maximum_value:
        count += 1
    if c == maximum_value:
        count += 1
    if a == maximum_value:
        if count == 1:
            v1 = 0
        else:
            v1 = 1
    else:
        v1 = maximum_value - a + 1
    if b == maximum_value:
        if count == 1:
            v2 = 0
        else:
            v2 = 1
    else:
        v2 = maximum_value - b + 1
    if c == maximum_value:
        if count == 1:
            v3 = 0
        else:
            v3 = 1
    else:
        v3 = maximum_value - c + 1
    print(v1, v2, v3)