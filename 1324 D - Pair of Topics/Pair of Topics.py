
def search(left, right, arr, idx):
    while left < right:
        mid = (left + right)//2
        if arr[idx] + arr[mid] > 0:
            right = mid
        else:
            left = mid + 1
    return left


n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
c = [v1 - v2 for v1, v2 in zip(a, b)]
c.sort()
res = 0
for i in range(1, len(c)):
    res += i - search(0, i, c, i)
print(res)