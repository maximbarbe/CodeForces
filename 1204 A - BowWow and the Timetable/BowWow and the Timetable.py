n = int(input(), 2)

time = 1
res = 0
while True:
    if time < n:
        res += 1
        time *= 4
    else:
        break
print(res)