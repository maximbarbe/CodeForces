from math import ceil, floor
while True:
    n, m, c = map(int, input().split())
    if n == m and m == 0 and c == 0:
        break
    n -= 7
    m -= 7
    res = 0
    if c == 1:
        number_of_white = ceil(m/2)
        number_of_black = floor(m/2)
    else:
        number_of_white = floor(m/2)
        number_of_black = ceil(m/2)
    print(number_of_white*ceil(n/2) + number_of_black*floor(n/2))