from math import floor

def f(v, k):
    res = v
    temp = k
    while floor(v/temp) != 0:
        res += floor(v/temp)
        temp *= k
    return res
        
        


n, k = map(int, input().split())

start = 1
end = k*n
while start < end:
    mid = (start + end)//2
    
    l = f(mid, k)
    if l < n:
        start = mid + 1
    else:
        end = mid
print(start)