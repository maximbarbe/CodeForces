k, d = map(int, input().split())
if d == 0:
    if k == 1:
        print(0)
    else:
        print("No solution")
else:
    print(f"{d}{'0'*(k-1)}")