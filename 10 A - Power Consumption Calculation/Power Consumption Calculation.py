n, p1, p2, p3, t1, t2 = map(int, input().split())




times = []
res = 0
for i in range(n):
    l, r = map(int, input().split())
    res += (r - l)*p1
    if i == 0:
        times.append(r)
    else:
        prev_end = times[-1]
        time_between = l - prev_end
        if time_between >= t2 + t1:
            res += (time_between - (t2 + t1))*p3
            res += (t2)*p2
            res += t1 * p1
        elif time_between >= t1:
            res += (time_between - t1)*p2
            res += t1 * p1
        else:
            res += time_between * p1
        times.append(r)
print(res)