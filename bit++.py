res = 0
n = int(input())
for i in range(n):
    line = input()
    if "++" in line:
        res += 1
    elif "--" in line:
        res -= 1
print(res)