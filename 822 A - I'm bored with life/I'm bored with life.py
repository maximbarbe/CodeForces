from math import factorial as f
 
n, m = map(int, input().split())
if n <= m:
    print(f(n))
else:
    print(f(m))