t = int(input())
for i in range(t):
    n = int(input())
    books = {"00": [], "01": [], "10":[], "11":[]}
    for i in range(n):
        time, type = input().split()
        books[type].append(int(time))
    for key in books.keys():
        books[key].sort()
    minimum = 10**9
    if books["11"]:
        minimum = min(minimum, books["11"][0])
    if books["01"] and books["10"]:
        minimum = min(minimum, books["01"][0] + books["10"][0])
    if minimum == 10**9:
        print(-1)
    else:
        print(minimum)