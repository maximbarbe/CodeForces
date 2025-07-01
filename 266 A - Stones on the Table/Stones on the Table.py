n = int(input())
chars = input()
res = 0
cur = chars[0]
for i in range(1, len(chars)):
    if chars[i] == cur:
        res += 1
    else:
        cur = chars[i]
print(res)