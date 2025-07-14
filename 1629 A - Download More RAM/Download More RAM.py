for i in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    for ai, bi in sorted([*zip(a, b)], key=lambda el: el[0]):
        if ai <= k:
            k += bi
        else:
            break
    print(k)
    