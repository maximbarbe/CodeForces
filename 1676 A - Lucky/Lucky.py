t = int(input())
for i in range(t):
    digits = [char for char in input()]
    if sum(map(int, digits[:3])) == sum(map(int, digits[3:])):
        print("YES")
    else:
        print("NO")