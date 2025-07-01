def end_on_dima(arr, n):
    fingers = sum(arr) %n
    if (fingers - 1)%n == 0:
        return True
    return False
    

n = int(input())
shown = [*map(int, input().split())]
res = 0
for i in range(1, 6):
    temp = [i] + shown
    if not end_on_dima(temp, n + 1):
        res += 1
print(res)