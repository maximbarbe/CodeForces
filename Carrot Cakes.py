n,t,k,d = map(int, input().split())
one_oven_time = 0
if n % k == 0:
    one_oven_time = t*n//k
else:
    one_oven_time = t*(n//k + 1)


prev_oven_1 = 0
prev_oven_2 = None
time = 0
cakes = 0
while cakes < n:
    if time == d:
        prev_oven_2 = d 
    else:

        if prev_oven_2 and time - prev_oven_2 == t:
            cakes += k
            prev_oven_2 = time
    if time - prev_oven_1 == t:
        cakes += k
        prev_oven_1 = time
    time += 1

time -= 1

if time < one_oven_time:
    print('YES')
else:
    print('NO')

