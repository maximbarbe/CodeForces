a, b = map(int, input().split())

f = min(a, b)
a -= f
b -= f
print(f, max(a //2, b//2))