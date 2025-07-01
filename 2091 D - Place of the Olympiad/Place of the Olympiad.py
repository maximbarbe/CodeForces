from math import ceil
 
t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    max_per_row = ceil(k/n)
    start = 1
    end = max_per_row
    prev_start = None
    prev_end = None
    while start != end:
        if start == prev_start and end == prev_end:
            break
        prev_end = end
        prev_start = start
        group_size = (start + end)//2
        if max_per_row % group_size == 0:
            n_groups = max_per_row//group_size
            if n_groups * group_size + n_groups - 1<= m:
                end = group_size
            else:
                start = group_size + 1
        else:
            n_big_groups =max_per_row//group_size
            reste = max_per_row - n_big_groups * group_size
            if n_big_groups * group_size + reste + n_big_groups <= m:
                end = group_size
            else:
                start = group_size + 1
    print(start)