from datetime import datetime

while True:
    n = int(input())
    if n == 0:
        break
    data= []
    days = 0
    res = 0 
    for i in range(n):
        d,m,y,c = map(int, input().split())
        data.append((datetime(y, m, d), c))
    for i in range(1, len(data)):
        if (data[i][0] - data[i - 1][0]).days == 1:
            days += 1
            res += data[i][1] - data[i - 1][1]
    print(days, res)