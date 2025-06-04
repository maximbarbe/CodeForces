a, b, c = map(int, input().split())
y = ((a*c)/b)**0.5
x = a/y
z = c/y
print(4*int(x) + 4*int(y) + 4*int(z))