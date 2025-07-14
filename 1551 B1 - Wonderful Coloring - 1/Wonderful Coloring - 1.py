from collections import Counter


def red(s):
    red = 0
    green = 0
    c = Counter(s)
    for char, freq in c.most_common(None):
        if freq > 1:
            red += 1
            green += 1
        else:
            if red == green:
                red += 1
            else:
                green += 1
    if red == green:
        return red
    return red - 1


t = int(input())
for i in range(t):
    s = input()
    print(red(s))