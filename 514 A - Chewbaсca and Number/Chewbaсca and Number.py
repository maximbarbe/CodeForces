num = [*map(int, input())]
for i in range(len(num)):
    if i == 0 and num[i] == 9:
        continue
    if num[i] > 4:
        num[i] = 9 - num[i]

print(int("".join(map(str, num))))