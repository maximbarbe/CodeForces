k, l, m, n = map(int, input().split())
vals = [k, l, m, n]
vals.sort()
k, l, m, n = vals
print((l-m+k)//2, (k + m - l)//2, (m -k + l)//2)