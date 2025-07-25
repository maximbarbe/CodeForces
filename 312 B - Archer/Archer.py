a, b, c, d = map(int, input().split())
k = (b*d - b*c - d*a + a*c)/(b*d)

print((a/b)*(1/(1-k)))