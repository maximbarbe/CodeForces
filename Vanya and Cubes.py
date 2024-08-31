n = int(input())
levels = [0]
while levels[-1] < 1000:
    levels.append(levels[-1] + len(levels))
needed_for_pyramid = [0]
for i in range(1, len(levels)):
    needed_for_pyramid.append(needed_for_pyramid[-1] + levels[i])
for i in range(len(needed_for_pyramid)):
    if n < needed_for_pyramid[i]:
        print(i - 1)
        exit(0)