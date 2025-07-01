n = int(input())
res = []
start = 1
end = n**2
while start < end:
    res.append([start, end])
    start += 1
    end -= 1
for v in res:
    print(*v)