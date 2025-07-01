for i in range(5):
    row = [*map(int, input().split())]
    for j in range(5):
        if row[j] == 1:
            res = abs(2 - i) + abs(2 - j)
print(res)