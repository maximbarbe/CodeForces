t = int(input())
for i in range(t):
    l,r,a = map(int, input().split())
    if r - r%a - 1 >= l:
        other = r - r%a - 1
        print(max(r//a + r%a, other//a + other%a))
    else:
        print(r//a + r%a)