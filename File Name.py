n = int(input())
count = 0
res = 0
for char in input():
    match char:
        case "x":
            count += 1
        case _:
            count = 0
    if count >= 3:
        res += 1
print(res)