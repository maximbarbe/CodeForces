t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    digits = {
        0:3,
        3:1,
        1:1,
        2:2,
        5:1 
    }
    counter = 0
    for v in vals:
        counter += 1
        if v in [0, 1, 2, 3, 5]:
            if digits[v] != 0:
                digits[v] -= 1
        for key, val in digits.items():
            if val == 0:
                continue
            else:
                break
        else:
            print(counter)
            break
    else:
        print(0)