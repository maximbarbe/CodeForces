
def sort(arr_a, arr_b):
    if not arr_a:
        return ([], [])
    idx = len(arr_a)//2
    pivot_a = arr_a[idx]
    pivot_b = arr_b[idx]
    left_a = []
    right_a = []
    left_b = []
    right_b = []
    for i in range(len(arr_a)):
        if i != idx:
            if arr_a[i] <= pivot_a:
                left_a.append(arr_a[i])
                left_b.append(arr_b[i])
            else:
                right_a.append(arr_a[i])
                right_b.append(arr_b[i])

    left_a, left_b = sort(left_a, left_b)
    right_a, right_b = sort(right_a, right_b)
    left_a.append(pivot_a)
    left_a.extend(right_a)
    left_b.append(pivot_b)
    left_b.extend(right_b)
    return (left_a, left_b)
    


t = int(input())
for i in range(t):
    n = int(input())
    a = [*map(int,input().split())]
    b = [*map(int,input().split())]
    a, b = sort(a, b)
    print(*a)
    print(*b)