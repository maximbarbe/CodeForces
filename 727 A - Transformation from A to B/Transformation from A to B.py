a, b = map(int, input().split())
nums = []
while a != b:
    nums.append(b)
    if b < a:
        print("NO")
        exit()
    if b%10 == 1:
        b = (b - 1)//10
    elif b % 2 == 0:
        b = b//2
    else:
        print("NO")
        exit()
nums.append(b)
print("YES")
print(len(nums))
print(*nums[::-1])