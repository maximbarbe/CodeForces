lucky_nums = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
n = int(input())
for val in lucky_nums:
    if n % val == 0:
        print("YES")
        exit()
else:
    print("NO")