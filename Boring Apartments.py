from bisect import bisect_left

aparts = []
for v in ['1', '2', '3', '4', "5", "6", "7", "8", "9"]:
    for i in range(1, 5):
        aparts.append(v*i)
        
        
t = int(input())
for i in range(t):
    target = input()
    res = 0
    for v in aparts:
        res += len(v)
        if v == target:
            print(res)
            break