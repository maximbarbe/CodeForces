from math import comb, floor
 
n, m = map(int, input().split())
 
print(m*comb(floor(n/m), 2) if n%m == 0 else (m-n%m)*comb(floor(n/m), 2) + (n%m)*comb(floor(n/m) + 1, 2),comb(n-m+1, 2))