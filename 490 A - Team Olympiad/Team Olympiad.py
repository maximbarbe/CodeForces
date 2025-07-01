n = int(input())
skills = [*map(int, input().split())]
ones = []
twos = []
thirds = []
for i in range(len(skills)):
    match skills[i]:
        case 1:
            ones.append(i)
        case 2:
            twos.append(i)
        case _:
            thirds.append(i)
print(min(len(ones), len(twos), len(thirds)))
for i in range(min(len(ones), len(twos), len(thirds))):
    print(ones[i] + 1, twos[i] + 1, thirds[i] + 1)