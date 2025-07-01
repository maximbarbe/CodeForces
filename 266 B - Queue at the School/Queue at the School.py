n, t = map(int, input().split())
pos = [char for char in input()]
for i in range(t):
    j = 0
    while j < n -1:
        if pos[j] == "B" and pos[j + 1] == "G":
            pos[j], pos[j + 1] = pos[j + 1], pos[j]
            j += 2
        else:
            j +=1
print("".join(pos))