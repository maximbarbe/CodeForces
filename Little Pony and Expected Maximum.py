m, n = map(int, input().split())
res = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        res += i*pow(i-1, n-j)
    


print(res/pow(m, n))