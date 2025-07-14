t = int(input())
for i in range(t):
    n = int(input())
    l = len(bin(n)) - 2
    print(int("0" + "1" * (l-1), 2))