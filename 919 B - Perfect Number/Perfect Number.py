

k = int(input())
cur = 18
while k != 0:
    cur += 1
    s = sum([int(d) for d in str(cur)])
    if s == 10:
        k -= 1
        cur += 5
    elif s > 10:
        cur //= 10
        cur += 1
        cur *= 10
        cur -= 1
        
print(cur - 5)