t = int(input())
for i in range(t):
    n = int(input())
    ones = [*map(int, input().split())].count(1)
    print(1 if ones % 2 == 1 else 0, min(ones, 2*n - ones))