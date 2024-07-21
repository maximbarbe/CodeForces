n = int(input())
m = 0
c = 0
for i in range(n):
    mish, chris = map(int, input().split())
    if mish > chris:
        m += 1
    elif chris > mish:
        c += 1
if m > c:
    print("Mishka")
elif c > m:
    print("Chris")
else:
    print("Friendship is magic!^^")