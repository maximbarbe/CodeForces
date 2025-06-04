
def get_difficulty(arr):
    return max([arr[i + 1] - arr[i] for i in range(len(arr) - 1)])

n = int(input())
vals = [*map(int, input().split())]
minimum = 1000
for i in range(1, len(vals) - 1):
    minimum = min(minimum, get_difficulty(vals[:i] + vals[i+1:]))
print(minimum)