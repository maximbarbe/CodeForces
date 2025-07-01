n = int(input())
number = input()
for c in number:
    if c not in "47":
        print("NO")
        exit()
if sum([int(c) for c in number[:n//2]]) == sum([int(c) for c in number[n//2:]]):
    print("YES")
else:
    print("NO")