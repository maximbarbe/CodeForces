from collections import defaultdict

n = int(input())
seen = defaultdict(lambda:False)
nums = []
cur = 1
while True:
    if n == 0:
        break
    if n - cur >= 0:
        nums.append(cur)
        seen[cur] = True
        n -= cur
        
        cur += 1
        
    else:
        nums.pop()
        
        nums.append(n + cur - 1)
        break
print(len(nums))
print(*nums)