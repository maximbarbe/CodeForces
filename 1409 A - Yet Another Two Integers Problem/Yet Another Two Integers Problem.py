t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    diff = abs(b - a)
    tens = abs(b - a)//10
    diff -= tens * 10
    if diff != 0:
        print(tens + 1)
    else:
        print(tens)