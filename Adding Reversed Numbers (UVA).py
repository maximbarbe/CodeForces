t =int(input())
for i in range(t):
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    res = str(a + b)[::-1].lstrip("0")
    if res == "":
        res = "0"
    print(res)