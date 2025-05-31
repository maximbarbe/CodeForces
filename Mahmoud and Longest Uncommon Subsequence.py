a = input()
b = input()
if len(a) != len(b):
    print(max(len(a), len(b)))
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print(len(a))
            exit()
    else:
        print(-1)