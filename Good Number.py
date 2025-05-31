n, k = map(int, input().split())
res = 0
for i in range(n):
    s = input()
    for digit in range(0, k + 1):
        if str(digit) not in s:
            break
    else:
        res += 1
print(res)