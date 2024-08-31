color = False
r, c = map(int, input().split())
for i in range(r):
    pixels = input().split()
    for char in pixels:
        if char in "CMY":
            color = True
            
print("#Color" if color else '#Black&White')