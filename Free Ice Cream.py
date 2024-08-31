q, x= map(int, input().split())
d = 0
for i in range(q):
    op, num = input().split()
    num = int(num)
    match op:
        case "-":
            if num > x:
                d += 1
            else:
                x -= num

        case _:
            x += num

            
print(x, d)