from collections import defaultdict

t = int(input())
for i in range(t):
    n = int(input())
    seen = defaultdict(lambda:0)
    vals = [*map(int, input().split())]
    mean = sum(vals)/n
    target = sum(vals) - mean*(n-2)
    if int(target) != target:
        print(0)
        continue
    target = int(target)
    res = 0
    for i in range(len(vals)):
        res += seen[target - vals[i]]
        seen[vals[i]] += 1
    print(res)