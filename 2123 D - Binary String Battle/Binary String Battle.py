t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()
    num_zeros = s.count("0")
    if k + num_zeros >= n:
        print("Alice")
    elif k > n // 2:
        print("Alice")
    else:
        print("Bob")