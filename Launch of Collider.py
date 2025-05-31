from math import ceil
n =int(input())
string = input()
pos = [*map(int, input().split())]
minimum = 10**9 + 1
for i in range(len(string) - 1):
    if string[i] == 'R' and string[i + 1] == "L":
        minimum = min(minimum, ceil((pos[i + 1] - pos[i])/2))
if minimum == 10**9 + 1:
    print(-1)
else:
    print(minimum)