n = int(input())
s = input()
rooms = ["0"]*10
l = 0
r = 9
for c in s:
    if c == "L":
        rooms[l] = "1"
    elif c == "R":
        rooms[r] = "1"
    else:
        rooms[int(c)] = "0"
    l = 0
    r = 9
    while l != 10 and rooms[l] == "1":
        l += 1
    while r != -1 and rooms[r] == "1":
        r -= 1
print("".join(rooms))