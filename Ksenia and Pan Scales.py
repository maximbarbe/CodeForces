data = input().split("|")
left = data[0]
right = data[1]
chars = input()
for c in chars:
    if len(left) <= len(right):
        left += c
    else:
        right += c
if len(left) != len(right):
    print("Impossible")
else:
    print(f"{left}|{right}")