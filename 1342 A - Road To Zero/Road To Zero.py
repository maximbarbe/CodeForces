t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    print(min(x*a + y*a, min(x, y)*b + (max(x, y) - min(x, y))*a))