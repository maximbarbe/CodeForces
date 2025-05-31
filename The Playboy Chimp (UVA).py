n = int(input())
heights = [*map(int, input().split())]
q = int(input())
queries = [*map(int, input().split())]
for q in queries:
    smaller_than = None
    prev_s = prev_e = None
    start = 0
    end = n - 1
    while start != end:
        mid = (start + end)//2
        if heights[mid] < q:
            start = mid
        else:
            end = mid - 1
        if prev_s == start and prev_e == end:
            break
    
        prev_s = start
        prev_e = end
    if start == end and heights[start] < q:
        smaller_than = heights[start]
    else:
        minimum = 0
        for i in range(start, end + 1):
            if heights[i] < q and heights[i] > minimum:
                minimum = heights[i]
        if minimum == 0:
            smaller_than = "X"
        else:
            smaller_than = minimum
    taller_than = None
    prev_s = prev_e = None
    start = 0
    end = n - 1
    while start != end:
        mid = (start + end)//2
        if heights[mid] > q:
            end = mid
        else:
            start = mid + 1
        if prev_s == start and prev_e == end:
            break
    
        prev_s = start
        prev_e = end
    if start == end and heights[start] > q:
        taller_than = heights[start]
    else:
        maximum = 2**31
        for i in range(start, end + 1):
            if heights[i] > q and heights[i] < maximum:
                maximum = heights[i]
        if maximum == 2**31:
            taller_than = "X"
        else:
            taller_than = maximum
    print(smaller_than, taller_than)