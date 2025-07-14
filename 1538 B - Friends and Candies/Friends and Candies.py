def possible(arr, prefix_sum, k, each):
    surplus = prefix_sum[k] - k*each
    for i in range(len(arr) -1, k, -1):
        if arr[i] > each:
            return True
        elif arr[i] < each:
            if surplus - (each-arr[i]) < 0:
                return False
            surplus -= (each-arr[i])
    return True
    

t = int(input())
for i in range(t):
    n = int(input())
    vals = sorted([*map(int, input().split())], reverse=True)
    prefix_sum = [0, vals[0]]
    for i in range(1, n):
        prefix_sum.append(vals[i] + prefix_sum[-1])
    if prefix_sum[-1]%n != 0:
        print(-1)
        continue
    else:
        each = prefix_sum[-1]//n
    left, right = 0, n
    while left < right:
        mid = (left + right)//2
        if not possible(vals, prefix_sum, mid, each):
            left = mid + 1
        else:
            right = mid
    print(left)
        
